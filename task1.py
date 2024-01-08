import openpyxl
from faker import Faker
from datetime import datetime
import random
import os

def generate_random_name():
    fake = Faker()
    return fake.first_name()

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")

wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = "TDSheet"

headers = ["Имя", "Текущая дата", "Текущее время"]

for col_num, header in enumerate(headers, 1):
    col_letter = openpyxl.utils.get_column_letter(col_num)
    sheet[f"{col_letter}1"] = header

random_name = generate_random_name()
sheet["A2"] = random_name
sheet["B2"] = current_date
sheet["C2"] = current_time

random_number = random.randint(100, 999)
file_name = f"{random_name}_{current_date}_{random_number}.xlsx"


folder_path = os.path.join(os.path.expanduser("~"), "Documents", "skcu")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, file_name)

wb.save(file_path)

print(f"Файл успешно создан и сохранен по пути: {file_path}")
