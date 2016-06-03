"""docstring here."""
import csv
# import re
# import string


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
        # full_address = string.split(item['address'], ' ', 1)
        # zip_code = full_address[0]
        # city = string.split(full_address[1], ' - ')[0]
        # street = string.split(full_address[1], ' - ')[1]
        # street = re.sub(r',', '', street)
        # street = re.sub(r'V\.', 'VIA', street)
        # street = re.sub(r'P\.ZZA', 'PIAZZA', street)

        self.albo_csv.writerow([
            item['surname'],
            item['name'],
            item['sid'],
            item['address']
            # street,
            # zip_code,
            # city
        ])
        return item
