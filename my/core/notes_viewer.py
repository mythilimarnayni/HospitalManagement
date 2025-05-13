# src/notes.py

import csv

class NoteDatabase:
    def __init__(self, notes_file='./data/Notes.csv'):
        self.notes_file = notes_file

    def get_note_by_patient_and_visit(self, patient_id, visit_id):
        notes = []
        try:
            with open(self.notes_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if (
                        row.get('Patient_ID', '').strip() == patient_id.strip()
                        and row.get('Visit_ID', '').strip() == visit_id.strip()
                    ):
                        notes.append(row)
        except Exception as e:
            print("Error reading notes file:", e)
        return notes
