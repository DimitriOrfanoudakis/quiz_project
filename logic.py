import json
import random

class QuizLogic:
    def __init__(self, fragen_datei):
    
    #Initialisiert das Quiz mit Fragen aus einer JSON Datei.

    #Args:
    #    fragen_datei(str) mit dem Dateipfad der zu öffnenden JSON Datei
    #Raises:
    #    FileNotFoundError: Wenn die Datei nicht existiert
    #    json.JSONDecodeError: Wenn das JSON-Format nich stimmt
    #    ValueError: Wenn die Datei leer ist

        self.fragen = []
        self.aktuelle_frage = 0
        self.punktzahl = 0

        #JSON Laden
        try:
            with open(fragen_datei, 'r', encoding='utf-8') as f:
                daten = json.load(f)
                self.fragen = daten.get("fragen", [])
        except FileNotFoundError:
            raise FileNotFoundError(f'Datei "{fragen_datei}" konnte nicht gefunden werden!')
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError('JSON-Format ungültig!', e.doc, e.pos)
        
        if not self.fragen:
            raise ValueError('Keine Fragen in der Datei!')


        #Fragen mischen
        random.shuffle(self.fragen)

        #Antworten innerhalb der Fragen mischen
        for frage in self.fragen:
            random.shuffle(frage["antworten"])


    def get_question(self):
    # Gibt die aktuelle Frage mit ihren vier Antwortmöglichkeiten zurück
    # 
    # Returns:
    #         dict mit Schlüsseln 'id':int, 'text':str, 'antworten':list[dicts], 'frage_nummer':int, 'von_insgesamt:int'
    #         oder None wenn Quiz fertig
        if self.is_finished():
            return None
        
        frage = self.fragen[self.aktuelle_frage]

        # Anworten ohne 'richtig' Attribut 
        verdeckte_antworten = [
            {'text': antwort["text"]}
            for antwort in frage["antworten"]
        ]

        return {
            'id': frage["id"],
            'text': frage["text"],
            'antworten': verdeckte_antworten,
            'frage_nummer': self.aktuelle_frage + 1,
            'von_insgesamt': len(self.fragen)
        }





    def check_answer(self):
    # Prüft ob die gewöhlte Antwort richtig ist
    # Erhöht ggf. die Punktezahl
    # Lädt die nächste Frage
    # Args:
    #      gewaehlte_antwort_text (str): Der Text der gewählten Antwort
    # Returns:
    #      dict mit den Schlüsseln 'richtig':bool, 'richtige_antwort':str, 'punkte_erhalten':int, 'neue_punktzahl':int
        pass

    def get_score(self):
    # Gibt den aktuellen Punktestand zurück
    # Returns: 
    #         dict mit Schlüsseln 'punkte':int, 'von_insgesamt':int, 'prozent':float
        pass

    def is_finished(self):
    # Prüft ob bereits alle Fragen ausgelesen wurden
    # Returns:
    #         True, wenn fertig
    #         False, wenn noch Fragen offen sind
        return self.aktuelle_frage >= len(self.fragen)



