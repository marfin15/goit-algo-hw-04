def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_list = [line.strip().split(",") for line in file]
            keys = ["id", "name", "age"]
            result = []
            for values in cats_list:
                cats_dict = {keys[i]: values[i] if i != 2 else int(values[i]) for i in range(len(keys))}   
                result.append(cats_dict)
            return result
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

cats_info = get_cats_info("cats.txt")
if cats_info is not None:
    print(cats_info)