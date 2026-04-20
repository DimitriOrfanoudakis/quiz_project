import json
import random

class QuizLogic:

    #Konstruktor, Initialisiert das Quiz mit Fragen aus einer JSON Datei.

    #Args:
    #    fragen_datei(str) mit dem Dateipfad der zu öffnenden JSON Datei
    #Raises:
    #    FileNotFoundError: Wenn die Datei nicht existiert
    #    json.JSONDecodeError: Wenn das JSON-Format nich stimmt
    #    ValueError: Wenn die Datei leer ist
    def __init__(self, fragen_datei):    

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




    # Gibt die aktuelle Frage mit ihren vier Antwortmöglichkeiten zurück
    # 
    # Returns:
    #         dict mit Schlüsseln 'id':int, 'text':str, 'antworten':list[dicts], 'frage_nummer':int, 'von_insgesamt:int'
    #         oder None wenn Quiz fertig
    def get_question(self):

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




    # Prüft ob die gewöhlte Antwort richtig ist
    # Erhöht ggf. die Punktzahl
    # Lädt die nächste Frage
    # Args:
    #      gewaehlte_antwort_text (str): Der Text der gewählten Antwort
    # Returns:
    #      dict mit den Schlüsseln 'richtig':bool, 'richtige_antwort':str, 'punkte_erhalten':int, 'neue_punktzahl':int
    def check_answer(self, gewaehlte_antwort_text):
    
        if self.is_finished():
            return {
                'richtig': False,
                'richtige_antwort': None,
                'punkte_erhalten': 0,
                'neue_punktzahl': self.punktzahl
            }
        
        frage = self.fragen[self.aktuelle_frage]

        #Richtige Antwort suchen
        richtige_antwort_text = None
        ist_richtig = False
        
        for antwort in frage["antworten"]:
            if antwort["richtig"]:
                richtige_antwort_text = antwort["text"]
            
            if antwort["text"].strip().lower() == gewaehlte_antwort_text.strip().lower():
                ist_richtig = antwort["richtig"]
        
        # Punkte erhöhen bei richtiger Antwort
        if ist_richtig:
            self.punktzahl += 1
            punkte_erhalten = 1
        
        # Zur nächsten Frage
        self.aktuelle_frage += 1
        
        return{
            'richtig': ist_richtig,
            'richtige_antwort': richtige_antwort_text,
            'punkte_erhalten': punkte_erhalten,
            'neue_punktzahl': self.punktzahl
        }



    # Gibt den aktuellen Punktestand zurück
    # Returns: 
    #         dict mit Schlüsseln 'punkte':int, 'von_insgesamt':int, 'prozent':float
    def get_score(self):
    
        if not self.fragen:
            return {
                'punkte': 0,
                'von_insgesamt': 0,
                'prozent': 0.0
            }
        
        insgesamt = len(self.fragen)
        prozent = (self.punktzahl / insgesamt) * 100 if insgesamt > 0 else 0
        
        return {
            'punktzahl': self.punktzahl,
            'von_insgesamt': insgesamt,
            'prozent': round(prozent, 1)
        }



    # Prüft ob bereits alle Fragen ausgelesen wurden
    # Returns:
    #         True, wenn fertig
    #         False, wenn noch Fragen offen sind
    def is_finished(self):
    
        return self.aktuelle_frage >= len(self.fragen)



