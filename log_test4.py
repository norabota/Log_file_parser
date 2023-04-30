from datetime import datetime
from prettytable import PrettyTable

# Чтение файла
with open("sc_runtime.log", "r") as file:
    lines = file.read().splitlines()

# Создаем словарь, где ключ - ID, а значение - список строк
id_lines = {}
id_intervals = {}

current_id = None
for line in lines:
    if "info: Slot to run:" in line:
        if current_id is not None:
            t1 = datetime.strptime(id_lines[current_id][0][0:23], '%Y-%m-%d %H:%M:%S.%f')
            t2 = datetime.strptime(line[0:23], '%Y-%m-%d %H:%M:%S.%f')
            interval = (t2 - t1).total_seconds()

            if current_id not in id_intervals:
                id_intervals[current_id] = []
            id_intervals[current_id].append(interval)

        current_id = int(line.split(":")[-1].strip())
        if current_id not in id_lines:
            id_lines[current_id] = []
        id_lines[current_id].append(line.strip())


# Вывод результата:пары строк
slot_to_run = list(id_lines.values())
print("---------------------------------------------")
for i in range(len(slot_to_run) - 1):
    print(*slot_to_run[i])
    print(*slot_to_run[i+1])
    print("---------------------------------------------")

# Вывод результата:cоздаем таблицу
table = PrettyTable()
table.field_names = ["ID", "Intervals"]

# Добавляем данные в таблицу
for id in id_intervals:
    intervals = id_intervals[id]
    interval_str = "\n".join([f"{interval:.3f} seconds" for interval in intervals])
    table.add_row([id, interval_str])
print(table)
