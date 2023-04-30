def find_error_logs(filename, board):
    with open(filename, 'r') as f:
        lines = f.readlines()

        # создаем словарь для хранения строк, соответствующих каждому уникальному ID
        id_lines = {}

        # ищем  строки, содержащие подстроку вида "Sending command:"
        for line in lines:
            if f"info: {board} : Sending command:" in line:
                id = int(line.split(":")[-1].split()[0])  # айди находится в предпоследней части строки

                # добавляем строку в список, соответствующий данному ID
                if id not in id_lines:
                    id_lines[id] = []
                    id_lines[id].append(line.strip())

        # формируем пары строк для каждого уникального ID
        for id in id_lines:
            reply_line_found = False
            for line in lines:
                if f"info: {board} : Got reply: {id + 1} NAK" in line:
                    print(id_lines[id][0])
                    print(line.strip())
                    print("---------------------------------------------------------------------------------------")
                    reply_line_found = True
                    break
            if not reply_line_found:
                print(id_lines[id][0])
                print(
                    f"Не удалось найти строки с подстрокой 'info: {board} : Got reply: {id + 1} NAK' в файле {filename}")
                print("---------------------------------------------------------------------------------------")


board = input("Введите значение BOARD (grabber, wash, tip, reagents): ")
find_error_logs('sc_device_v.log', board)
