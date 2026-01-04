ip = input().strip()
parts = ip.split('.')

if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
    print("ДА")
else:
    print("НЕТ")
