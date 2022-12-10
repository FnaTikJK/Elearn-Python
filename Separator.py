import csv


class Spliter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def split(self):
        (years, list_naming) = self.find_rows_by_year_with_naming()
        self.create_csv_by_years(years, list_naming)
        return 10

    def find_rows_by_year_with_naming(self):
        years = {}
        with open(self.file_name, encoding='utf-8-sig') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    count += 1
                    list_naming = row
                else:
                    if "" in row or len(row) != len(list_naming):
                        continue
                    year = row[5][0:4]
                    if year not in years.keys():
                        years[year] = list()
                    years[year].append(row)
        return (years, list_naming)

    def create_csv_by_years(self, years, list_naming):
        for year in years:
            with open(f"./stats/{year}.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                file_writer.writerow(list_naming)
                for row in years[year]:
                    file_writer.writerow(row)


file_name = input("Введите название csv-исходника: ")
spliter = Spliter(file_name)
spliter.split()