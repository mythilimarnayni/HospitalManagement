# core/usage_audit.py

import csv
from datetime import datetime

class AuditTrail:
    def __init__(self, log_file='./data/session_log.csv'):
        self.log_file = log_file
        self.fields = ['user', 'role', 'action_time', 'activity']

    def record(self, user, role, activity):
        try:
            with open(self.log_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.fields)
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow({
                    'user': user,
                    'role': role,
                    'action_time': datetime.now().isoformat(),
                    'activity': activity
                })
        except Exception as e:
            print("Logging failed:", e)