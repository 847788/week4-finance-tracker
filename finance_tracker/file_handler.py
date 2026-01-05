import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def backup_data():
    backup_dir = "data/backup"
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_dir}/expenses_{timestamp}.json"

    with open(DATA_FILE, "r") as src, open(backup_file, "w") as dst:
        dst.write(src.read())
