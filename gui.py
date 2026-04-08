import tkinter as tk

root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")


aktuelle_frage ={
    "frage": "Was ist die Hauptstadt von Frankreich?",
    "optionen": ["Berlin", "Paris", "Madrid", "Rom"],
    "antwort": "Paris"
}

frage_label = tk.Label(root, text=aktuelle_frage["frage"], font=("Arial", 16))
frage_label.pack(pady=20)

def check_answer(checked, btn):
    if checked == aktuelle_frage["antwort"]:
        btn.config(bg="green")
    else:
        btn.config(bg="red")
    
    for b in buttons:
        b.config(state="disabled")
    
    next_button.config(state="normal") 

def next_question():
    print("Nächste Frage!")

buttons = []

for option in aktuelle_frage["optionen"]:
    btn = tk.Button(root, text=option, font=("Arial", 20), width=20)
    btn.config(command=lambda o=option, b=btn: check_answer(o, b))
    btn.pack(pady=5)
    buttons.append(btn)

next_button = tk.Button(root, text="Nächste Frage", font=("Arial", 14), 
                        command=next_question, state="disabled")
next_button.pack(pady=20)


root.mainloop()

