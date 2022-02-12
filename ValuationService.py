import csv
from typing import Union


class CSVReader:

    @staticmethod
    def read_csv(file: str) -> list[dict]:
        result: Union[list, dict] = []
        with open(file, mode='r') as file:
            fieldnames = file.readline().strip().split(',')
            f = csv.DictReader(file, fieldnames=fieldnames, delimiter=',')
            for line in f:
                result.append(line)
        return result

    @staticmethod
    def csv_data_to_dict(data: list[dict]) -> dict:
        fieldnames = list(data[0].keys())
        if len(fieldnames) == 2:
            result = {x[fieldnames[0]]: x[fieldnames[1]] for x in data}
            return result
        raise TypeError('wrong data format: too many keys to wrap list into dict')

    @staticmethod
    def write_csv(file: str, data: list[dict]):
        try:
            fieldnames = list(data[0].keys())
            with open(file, mode='w') as file:
                result = csv.DictWriter(
                    f=file,
                    fieldnames=fieldnames,
                    delimiter=',',
                    lineterminator='\n')
                result.writeheader()
                result.writerows(data)
        except (AssertionError, KeyError):
            raise ValueError('wrong data format: list[dict] is expected')


class ValuationService:
    currencies: dict
    data: list
    matching: dict

    def __init__(self, currencies_file_path: str, data_file_path: str, matching_file_path: str) \
            -> None:
        curr = CSVReader.read_csv(currencies_file_path)
        self.currencies = CSVReader.csv_data_to_dict(curr)

        self.data = CSVReader.read_csv(data_file_path)

        match = CSVReader.read_csv(matching_file_path)
        self.matching = CSVReader.csv_data_to_dict(match)

    def calculate_total_price(self) -> None:
        for row in self.data:
            price = int(row['price'])
            quantity = int(row['quantity'])
            currency = float(self.currencies[row['currency']])
            row['total_price'] = price * quantity * currency

    def filter_and_sort_products_matching_id(self, id: int) -> list[dict]:
        matching_products = filter(lambda row: row['matching_id'] == id, self.data)
        matching_products = sorted(matching_products, key=lambda row: row['total_price'],
                                   reverse=True)
        return matching_products

    def choose_n_best_products(self, n: int, products: list[dict]) -> list[dict]:
        top_prods = []
        list_of_prices = [p['total_price'] for p in products]
        avg_price = sum(list_of_prices) / len(list_of_prices)
        n = min(len(products), int(n))
        ignored_products = len(list_of_prices) - n
        for i, p in enumerate(products[: n]):
            p.pop('id')
            p.pop('price')
            p.pop('quantity')
            p['avg_price'] = avg_price
            p['ignored_products_count'] = ignored_products
            p = dict(sorted(p.items(), key=lambda item: item[0]))
            top_prods.append(p)
        return top_prods

    def run(self, output_file_path: str) -> None:
        top_products = []
        self.calculate_total_price()
        for id, count in self.matching.items():
            matching_products = self.filter_and_sort_products_matching_id(id)
            top_products += self.choose_n_best_products(count, matching_products)
        CSVReader.write_csv(output_file_path, top_products)


if __name__ == '__main__':
    vs = ValuationService('currencies.csv', 'data.csv', 'matchings.csv')
    vs.run('output.csv')
