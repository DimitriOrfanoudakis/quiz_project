import tkinter as tk
#/ ______________________________
#/ Hauptfenster
#/ ______________________________
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")

#/ ______________________________
#/ Testfragen
#/ ______________________________
fragen = [
    {
        "frage": "Was ist die Hauptstadt von Frankreich?",
        "optionen": ["Berlin", "Paris", "Madrid", "Rom"],
        "antwort": "Paris"
    },
    {
        "frage": "Wie viele Seiten hat ein Hexagon?",
        "optionen": ["5", "6", "7", "8"],
        "antwort": "6"
    },
    {
        "frage": "Was ist 7 x 8?",
        "optionen": ["54", "56", "58", "52"],
        "antwort": "56"
    }
]

aktueller_index = 0
aktuelle_frage = fragen[aktueller_index]
#/ ______________________________
#/ GUI-Elemente
#/ ______________________________

#/ Frage x von x
nummer_label = tk.Label(root, text=f"Frage {aktueller_index + 1} von {len(fragen)}", font=("Arial", 12))
nummer_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


frage_label = tk.Label(root, text=aktuelle_frage["frage"], font=("Arial", 16))
frage_label.pack(pady=20)

#/ Buttons für Antwortoptionen
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = []

#/ Funktion,um die Antwort zu checken und die Buttons entsprechend zu färben
def check_answer(checked, btn):
    if checked == aktuelle_frage["antwort"]:
        btn.config(bg="green")
    else:
        btn.config(bg="red")

    for b in buttons:
        b.config(state="disabled")

    next_button.config(state="normal")

#/ Funktion, um zur nächsten Frage zu wechseln / Quiz beenden, wenn alle Fragen beantwortet wurden
def next_question():
    global aktueller_index, aktuelle_frage

    aktueller_index += 1
#/ Wenn alle Fragen beantwortet wurden, Quiz beenden
    if aktueller_index >= len(fragen):
        frage_label.config(text="Quiz beendet! Danke fürs Mitspielen.")
        nummer_label.config(text="")
        for btn in buttons:
            btn.grid_forget()
        next_button.pack_forget()
        return
# Neue Frage laden
    aktuelle_frage = fragen[aktueller_index]
# Label und Antwortbuttons aktualisieren passend zur Frage
    frage_label.config(text=aktuelle_frage["frage"])
    nummer_label.config(text=f"Frage {aktueller_index + 1} von {len(fragen)}")

    for i, btn in enumerate(buttons):
        option_text = aktuelle_frage["optionen"][i]
        btn.config(
            text=option_text,
            bg="SystemButtonFace",
            state="normal"
        )
        btn.config(command=lambda o=option_text, b=btn: check_answer(o, b))
        
# Buttons für die nächste Frage deaktivieren, bis eine Antwort ausgewählt wird
    next_button.config(state="disabled")

# Buttons für die Frage erstellen
def create_button(option, row, col):
    btn = tk.Button(button_frame, text=option, font=("Arial", 16), width=20)
    btn.grid(row=row, column=col, pady=5)
    btn.config(command=lambda o=option, b=btn: check_answer(o, b))
    return btn

# Buttons für die aktuelle Frage erstellen + Sortierung in 2 Spalten
for i, option in enumerate(aktuelle_frage["optionen"]):
    row = i // 2
    col = i % 2
    btn = create_button(option, row, col)
    buttons.append(btn)
    
# Weiter-Button
next_button = tk.Button(root, text="Nächste Frage", font=("Arial", 14),
                        command=next_question, state="disabled")
next_button.pack(pady=20)

root.mainloop()
