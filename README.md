# HospitalManagement

#

## 📁 Project Structure

```
clinical_data_ui/
├── main.py
├── src/
│   ├── ui.py
│   ├── user.py
│   ├── patient.py
│   ├── notes.py
│   ├── logger.py
│   ├── stats.py
├── data/
│   ├── Credentials.csv
│   ├── Patient_data.csv
│   ├── Notes.csv
│   └── usage_log.csv
```

## ✅ Features

- Role-based login (Admin, Nurse, Clinician, Management)
- Add, retrieve, and remove patients
- Count number of visits by date
- View clinical notes for a given patient and visit
- Log all user actions to `usage_log.csv`
- Generate statistics on patient age distribution

## 🚀 Getting Started

### 1. Install dependencies
```
pip install pandas matplotlib
```

### 2. Run the application
```
python main.py
```

## 🗂️ Required CSV Files (in `data/` folder)

### Credentials.csv
```csv
username,password,role
admin,admin123,admin
nurse1,pass123,nurse
clinician1,pass456,clinician
manager1,mgmtpass,management
```

### Patient_data.csv
```csv
Patient_ID,Visit_ID,Visit_time,Visit_department,Gender,Race,Age,Ethnicity,Insurance,Zip code,Chief complaint,Note_ID,Note_type
```

### Notes.csv
```csv
Patient_ID,Visit_ID,Note_ID,Note_text
```

---

## 👥 Roles & Access

| Role        | Permissions                        |
|-------------|-------------------------------------|
| Admin       | Count visits only                  |
| Nurse       | All except statistics              |
| Clinician   | All except statistics              |
| Management  | Generate statistics only           |

---

## 📊 Statistics Output
- A histogram of patient ages saved as `age_distribution.png`

## 📌 Notes
- Data files must be in the `data/` directory
- Encoding should be UTF-8 to prevent read errors
- Visit filtering in Notes works with `Patient_ID` + `Visit_ID
