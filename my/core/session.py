# core/session.py

import csv

class Account:
    def __init__(self, uid, role):
        self.uid = uid
        self.role = role

class SessionManager:
    def __init__(self, auth_file='./data/Credentials.csv'):
        self.auth_file = auth_file

    def validate_user(self, uid, password):
        try:
            with open(self.auth_file, newline='', encoding='utf-8') as csvfile:
                entries = csv.DictReader(csvfile)
                for user in entries:
                    if user['username'].strip() == uid and user['password'].strip() == password:
                        return Account(uid, user['role'].strip())
        except Exception as e:
            print("Error reading credentials:", e)
        return None