import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(file_name: str, output_name: str = "output.json", delimiter: str = ",", indent: int = 4) -> None:
    try:
        with open(file_name, "r") as csv_f:
            reader = csv.DictReader(csv_f, delimiter=delimiter)
            with open(output_name, "w") as json_f:
                output_data = []
                for dict in reader:
                    output_data.append(dict)
                json.dump(output_data, json_f, indent=indent)
    except:
            print("Ошибка конвертации")



if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
