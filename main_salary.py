def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [line.strip().split(",") for line in file]
            salaries_int = [int(salary[1]) for salary in salaries]
            total = sum(salaries_int)
            average = total // len(salaries_int)
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

total, average = total_salary("total_salary.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    

