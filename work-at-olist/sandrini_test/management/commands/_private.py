import csv
import os


class CsvImporter:

    def __init__(self, csv_path=None):
        if csv_path:
            if os.path.isfile(csv_path):
                self.csv_path = csv_path

    def read(self):
        if self.csv_path:
            with open(self.csv_path, newline="") as csvfile:
                spamreader = csv.reader(csvfile, delimiter="/", quotechar="|")
                for index, row in enumerate(spamreader):
                    if index == 0 and row[0] != "Category":
                        raise Exception("Invalid Format - the first column is not 'Category' - %s" % row[0])
                    