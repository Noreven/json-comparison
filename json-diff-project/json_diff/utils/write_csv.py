import csv


def write_csv(data: dict):
    with open("output.csv", "w+", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(data)
