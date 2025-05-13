# core/insights.py

import pandas as pd
import matplotlib.pyplot as plt

class InsightEngine:
    def __init__(self, file_path='./data/Patient_data.csv'):
        self.file_path = file_path

    def visualize_age_distribution(self):
        try:
            df = pd.read_csv(self.file_path)
            df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
            df.dropna(subset=['Age'], inplace=True)
            df['Age'].hist(bins=10, color='skyblue', edgecolor='black')
            plt.title("Patient Age Distribution")
            plt.xlabel("Age")
            plt.ylabel("Number of Patients")
            plt.tight_layout()
            plt.savefig('./data/insight_age_histogram.png')
            plt.close()
        except Exception as e:
            print("Failed to generate statistics:", e)
