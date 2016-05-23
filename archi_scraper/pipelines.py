import csv


class AlboToCSVPipeline(object):

    def __init__(self):
        self.albo_csv = csv.writer(open('albo.csv', 'wb'))
        self.albo_csv.writerow([
            'COGNOME',
            'NOME',
            'CODICE FISCALE',
            'INDIRIZZO',
            'CAP',
            'COMUNE'
        ])

    def process_item(self, item, spider):
        self.albo_csv.writerow([
            item['surname'],
            item['name'],
            item['sid'],
            item['address'],
            item['zip_code'],
            item['city']
        ])
        return item
