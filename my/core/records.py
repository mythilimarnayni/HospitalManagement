# core/records.py

import csv
from uuid import uuid4

class PatientHandler:
    def __init__(self, patient_file='./data/Patient_data.csv'):
        self.patient_file = patient_file
        self.fields = ["Patient_ID", "Visit_ID", "Visit_time", "Visit_department",
                       "Gender", "Race", "Age", "Ethnicity", "Insurance", "Zip code",
                       "Chief complaint", "Note_ID", "Note_type"]

    def fetch_all(self):
        try:
            with open(self.patient_file, newline='', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        except:
            return []

    def store_all(self, patient_data):
        with open(self.patient_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(patient_data)

    def insert_record(self, entry):
        entry["Visit_ID"] = str(uuid4())[:8]
        data = self.fetch_all()
        data.append(entry)
        self.store_all(data)

    def erase_patient(self, patient_id):
        data = self.fetch_all()
        updated = [rec for rec in data if rec["Patient_ID"] != patient_id]
        self.store_all(updated)

    def get_latest_visit(self, patient_id):
        data = self.fetch_all()
        matches = [rec for rec in data if rec["Patient_ID"] == patient_id]
        if not matches:
            return None
        return sorted(matches, key=lambda x: x["Visit_time"], reverse=True)[0]

    def total_visits_on(self, date_str):
        return sum(1 for entry in self.fetch_all() if entry["Visit_time"] == date_str)