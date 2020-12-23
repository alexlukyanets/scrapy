import csv

filename = 'permits.csv'
fieldnames = ['permit_number', 'permit_type', 'application_date', 'issue_date',
              'street', 'city', 'state', 'description', 'fee', 'contacts', 'cost']

with open(filename, 'a+', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


class PermitsCrawlerPipeline(object):
    def process_item(self, item, spider):
        with open(filename, 'a+', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(item)
        return item
