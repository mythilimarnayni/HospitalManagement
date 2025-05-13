# core/interface.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from core.session import SessionManager
from core.records import PatientHandler
from core.notes_viewer import NoteDatabase
from core.usage_audit import AuditTrail
from core.insights import InsightEngine

class HealthRecordUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Record Manager")
        self.root.geometry("580x500")
        self.root.configure(bg="#f0f2f5")

        self.auth = SessionManager()
        self.records = PatientHandler()
        self.notes = NoteDatabase()
        self.audit = AuditTrail()
        self.insight = InsightEngine()
        self.current = None

    def start(self):
        self.show_login()
        self.root.mainloop()

    def show_login(self):
        self.clear_ui()
        tk.Label(self.root, text="Login to Hospital Records", font=("Segoe UI", 16, "bold"), bg="#f0f2f5").pack(pady=20)

        frame = tk.Frame(self.root, bg="#f0f2f5")
        frame.pack()

        tk.Label(frame, text="Username", bg="#f0f2f5").grid(row=0, column=0, pady=5, sticky="e")
        user_entry = tk.Entry(frame)
        user_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Password", bg="#f0f2f5").grid(row=1, column=0, pady=5, sticky="e")
        pass_entry = tk.Entry(frame, show="*")
        pass_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.root, text="Login", bg="#3498db", fg="white", width=20,
                  command=lambda: self.login(user_entry.get(), pass_entry.get())).pack(pady=15)

    def login(self, user, pwd):
        result = self.auth.validate_user(user, pwd)
        if result:
            self.current = result
            self.audit.record(user, result.role, "LOGIN")
            self.show_dashboard()
        else:
            self.audit.record(user, "unknown", "FAILED_LOGIN")
            messagebox.showerror("Access Denied", "Invalid username or password.")

    def show_dashboard(self):
        self.clear_ui()
        tk.Label(self.root, text=f"Welcome {self.current.uid} ({self.current.role})",
                 font=("Segoe UI", 14, "bold"), bg="#f0f2f5").pack(pady=20)

        actions = {
            'clinician': [
                ("Add Patient", self.add_patient),
                ("Retrieve Patient", self.retrieve_patient),
                ("Remove Patient", self.remove_patient),
                ("Count Visits", self.count_visits),
                ("View Notes", self.view_notes)
            ],
            'nurse': [
                ("Add Patient", self.add_patient),
                ("Retrieve Patient", self.retrieve_patient),
                ("Remove Patient", self.remove_patient),
                ("Count Visits", self.count_visits),
                ("View Notes", self.view_notes)
            ],
            'admin': [
                ("Count Visits", self.count_visits)
            ],
            'management': [
                ("Generate Statistics", self.generate_statistics)
            ]
        }

        for label, func in actions.get(self.current.role, []):
            tk.Button(self.root, text=label, width=25, pady=6, bg="#2ecc71", fg="white", command=func).pack(pady=4)

        tk.Button(self.root, text="Exit", width=25, pady=6, bg="#e74c3c", fg="white", command=self.root.quit).pack(pady=20)

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_patient(self):
        fields = [
            ("Patient_ID", str), ("Visit_time", str), ("Visit_department", str),
            ("Gender", str), ("Race", str), ("Age", int),
            ("Ethnicity", str), ("Insurance", str), ("Zip code", str),
            ("Chief complaint", str), ("Note_ID", str), ("Note_type", str)
        ]

        entry = {}
        for label, typ in fields:
            val = simpledialog.askstring("Input", f"{label}:")
            if val is None:
                return
            try:
                entry[label] = typ(val)
            except:
                messagebox.showerror("Invalid Input", f"{label} must be {typ.__name__}")
                return

        self.records.insert_record(entry)
        self.audit.record(self.current.uid, self.current.role, f"ADD_PATIENT {entry['Patient_ID']}")
        messagebox.showinfo("Success", "Patient record added.")

    def retrieve_patient(self):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        record = self.records.get_latest_visit(pid)
        if record:
            info = "\n".join(f"{k}: {v}" for k, v in record.items())
            self.audit.record(self.current.uid, self.current.role, f"RETRIEVE {pid}")
            messagebox.showinfo("Patient Record", info)
        else:
            messagebox.showinfo("Not Found", "No records found.")

    def remove_patient(self):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        self.records.erase_patient(pid)
        self.audit.record(self.current.uid, self.current.role, f"REMOVE {pid}")
        messagebox.showinfo("Removed", f"Patient {pid} deleted.")

    def count_visits(self):
        dt = simpledialog.askstring("Date", "Enter Visit Date (YYYY-MM-DD):")
        total = self.records.total_visits_on(dt)
        self.audit.record(self.current.uid, self.current.role, f"VISIT_COUNT {dt}")
        messagebox.showinfo("Visit Count", f"Total visits on {dt}: {total}")

    def view_notes(self):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        vid = simpledialog.askstring("Visit ID", "Enter Visit ID:")
        notes = self.notes.get_note_by_patient_and_visit(pid, vid)
        if notes:
            output = "\n\n".join(f"Note {n['Note_ID']}:\n{n['Note_text']}" for n in notes)
            self.audit.record(self.current.uid, self.current.role, f"VIEW_NOTE {pid} {vid}")
            messagebox.showinfo("Clinical Notes", output)
        else:
            messagebox.showinfo("Not Found", "No notes found.")

    def generate_statistics(self):
        self.insight.visualize_age_distribution()
        self.audit.record(self.current.uid, self.current.role, "GENERATE_STATISTICS")
        messagebox.showinfo("Complete", "Statistics saved to insight_age_histogram.png")