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
            'INDIRIZZO'
        ])

    def process_item(self, item, spider):
        """docstring here."""
        archi = []

        for field in ['surname', 'name', 'sid', 'address']:
            if field in item:
                archi.append(item[field])
            else:
                archi.append('')

        self.albo_csv.writerow(archi)
        return item
