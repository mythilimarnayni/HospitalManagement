# Clinical Data Management System

This Python application provides a simple clinical data interface that allows users to:
- View and manage patient visit records
- Analyze clinical note content
- Track user session activity

##  Project Structure

```
my/
├── app_main.py               # Main entry point for launching the UI
├── core/                     # Core logic modules
│   ├── interface.py          # UI logic
│   ├── records.py            # Patient and visit record handling
│   ├── notes_viewer.py       # Viewing patient notes
│   ├── insights.py           # Data analysis & visualization
│   ├── session.py            # Session management
│   └── usage_audit.py        # Tracks user activity
├── data/                     # Data files
│   ├── Credentials.csv       # Username/password credentials
│   ├── Notes.csv             # Clinical notes
│   ├── Patient_data.csv      # Patient visit records
│   └── session_log.csv       # Logs of user activity
```

##  Setup & Execution

### Prerequisites

Ensure Python 3.10+ is installed. Required packages include:
- `pandas`
- `tkinter`

Install missing packages using:

```bash
pip install pandas
```

### Running the Application

Navigate to the `my` directory and run:

```bash
python app_main.py
```

This will launch the Tkinter-based GUI.

##  Login Credentials

Edit the `data/Credentials.csv` to manage user accounts. Example format:

```
Username,Password,Role
admin,admin123,admin
nurse,nurse123,nurse
```

##  Features

- Count and view patient visits
- Retrieve, add, or remove patient records
- View clinical notes by date
- Session logging for user audit trail


