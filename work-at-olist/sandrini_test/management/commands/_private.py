import csv
import os
from sandrini_test.models import Category, Channel

class CsvImporter:
    csv_path=None

    def __init__(self, channel, csv_path=None):
        self.channel, created = Channel.objects.get_or_create(name=channel)
        if not created:
            Category.objects.filter(channel=self.channel).delete()

        if csv_path:
            if os.path.isfile(csv_path):
                self.csv_path = csv_path
        else:
            print("Warning! csv path is None!")

    def process(self):
        if self.csv_path:
            with open(self.csv_path, newline="") as csvfile:
                spamreader = csv.reader(csvfile, delimiter="/", quotechar="|")

                for index, row in enumerate(spamreader):
                    if index == 0 and row[0] != "Category":
                        raise Exception("Invalid Format - the first column is not 'Category' - %s" % row[0])
                    if index > 0:
                        self.create_or_update_categories(row)

    def create_or_update_categories(self, categories_list):
        if len(categories_list) == 1:
            Category.objects.create(channel=self.channel, name=categories_list[0].strip())
            print("[%s] %s" % (self.channel, categories_list[0].strip()))
        else:
            if len(categories_list) > 2:
                top_category=Category.objects.get(name=categories_list[-2].strip(),
                                                  top_category__name=categories_list[-3].strip(),
                                                  channel=self.channel)
            else:
                top_category=Category.objects.get(name=categories_list[-2].strip(),
                                                  channel=self.channel, top_category=None)

            Category.objects.create(channel=self.channel, name=categories_list[-1].strip(),
                                    top_category=top_category)

            print("[%s] %s > %s" % (self.channel, top_category.name, categories_list[-1].strip()))