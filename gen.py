import csv


def genearate(filename):
    passwords = set() 
    years = range(1950, 2024)
    with open(filename) as file:
        reader = csv.DictReader(file, fieldnames=["name", "gender", "race"])
        next(reader)
        for row in reader:
            for year in years:
                if row["name"[:4]].isalpha():
                    passwords.add(row["name"][:4].upper() + str(year) + "\n")

    with open("passwords.txt", "w") as file:
        for password in sorted(passwords):
            file.write(password)


if __name__ == "__main__":
    genearate("male_names.csv")

