import json

# TODO решите задачу
def task(file_name) -> float:
    try:
        result = 0.0
        with open(file_name, "r") as f:
            data = json.load(f)
            for dict in data:
                result += dict["score"] * dict["weight"]
        return round(result, 3)
    except:
        return "Некорректные данные!"


print(task("input.json"))
