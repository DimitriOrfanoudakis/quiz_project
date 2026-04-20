import json
import random

class Quizlogic:
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
        self.punkte = 0

        #JSON Laden
        try:
            with open(fragen_datei, 'r', encoding='utf-8') as f:
                pass
        except:
            pass

        #Fragen mischen

        #Antworten innerhalb der Fragen mischen


        def get_question(self):
        # Gibt die aktuelle Frage mit ihren vier Antwortmöglichkeiten zurück
        # 
        # Returns:
        #         dict mit Schlüsseln 'id':int, 'text':str, 'antworten':list[str], 'frage_nummer':int, 'von_insgesamt:int'
        #         oder None wenn Quiz fertig
        # 
        # 
        # 
        # 
        # 
        #     
            pass

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
            pass



