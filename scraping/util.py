import csv

def row_exists_in_csv(filename: str, new_row: list):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if str(row) == str(new_row):
                    return True
    except FileNotFoundError:
        pass
    return False

def write(filename: str, new_row: list, max_length: int = 100):
    existing_data = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                existing_data.append(row)
    except FileNotFoundError:
        pass
    
    existing_data.append(new_row)
    
    if len(existing_data) > max_length:
        existing_data = existing_data[-max_length:]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(existing_data)

def write_to_csv_deinze(filename: str, date: str, price: str) -> bool:
    new_row = [date, price]

    if row_exists_in_csv(filename, new_row):
        print("Date already exists in CSV file. Skipping...")
        return False
    
    write(filename, new_row)
    return True

def write_to_csv_abc(filename: str, weeknr: str, price: str) -> bool:
    new_row = [weeknr, price]

    if row_exists_in_csv(filename, new_row):
        print("Week number already exists in CSV file. Skipping...")
        return False
    
    write(filename, new_row)
    return True