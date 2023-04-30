value = int(input("Введите значение: "))  # Передаём значение
with open('sc_device.log') as f:
    for line in f:
        if 'grabber : ntc reply = NTC,0000,0370,' in line:
            tttt = int(line.split(',')[-1])
            if tttt >= value:
                print('OK:', line.strip())
            else:
                print('ERR:', line.strip())
