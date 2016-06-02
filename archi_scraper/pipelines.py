"""docstring here."""
import csv


class AlboToCSVPipeline(object):
    """docstring here."""

    def __init__(self):
        """docstring here."""
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
        """docstring here."""
        print(item['surname'])
        print(item['name'])
        print(item['sid'])
        print(item['address'])

        # full_address = item['address']
        #
        # self.albo_csv.writerow([
        #     item['surname'],
        #     item['name'],
        #     item['sid'],
        #     item['address'],
        #     item['zip_code'],
        #     item['city']
        # ])
        return item
