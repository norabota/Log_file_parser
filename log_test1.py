with open('200731.LOG', 'r', encoding='UTF-16') as f:
    lines = f.readlines()

# Находим строку, содержащую подстроку "Worklist name"
worklist_name_line = None
for line in reversed(lines):
    if 'Worklist name' in line:
        worklist_name_line = line
        break

if worklist_name_line is None:
    print('Ошибка: не найдена строка с подстрокой "Worklist name"')
    exit(1)

# Находим индекс последней строки с идентификатором
last_id_line_idx = None
for idx, line in enumerate(reversed(lines)):
    if 'CYCLE complete' in line:
        last_id_line_idx = len(lines) - idx - 1
        break

if last_id_line_idx is None:
    print('Ошибка: не найдена строка с идентификатором')
    exit(1)

# Проверяем непрерывность идентификаторов
last_id = None
for line in lines[last_id_line_idx:]:
    if 'CYCLE complete' in line:
        id_str = line.split(' ')[-1].strip()
        if last_id is not None and int(id_str) != last_id + 1:
            print(f'Ошибка: идентификаторы не являются непрерывными: {last_id}, {id_str}')
            exit(1)
        last_id = int(id_str)
print('Идентификаторы являются непрерывными')

# Находим индекс строки с именем "Worklist name" и считаем количество строк вида "CYCLE complete"
cycle_complete_count = 0
for idx, line in enumerate(lines):
    if 'Worklist name' in line:
        # Получаем путь к файлу worklist
        worklist_path = 'C:' + line.split(':')[-1].strip()

        # Считаем количество строк вида "CYCLE complete" до следующей строки с именем "Worklist name"
        for next_line in lines[idx + 1:]:
            if 'Worklist name' in next_line:
                break
            if 'CYCLE complete' in next_line:
                cycle_complete_count += 1
        # Выводим результаты
        print(f'Файл worklist: {worklist_path} - Количество строк CYCLE complete: {cycle_complete_count}')
        cycle_complete_count = 0
