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


[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
