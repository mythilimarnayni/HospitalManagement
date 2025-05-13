# health_records_ui/app_main.py

from core.interface import HealthRecordUI

def launch():
    app = HealthRecordUI()
    app.start()

if __name__ == "__main__":
    launch()
