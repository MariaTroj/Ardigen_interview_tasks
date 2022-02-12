from ValuationService import ValuationService, CSVReader
import pytest


def test_valuation_service_class():
    vs = ValuationService('test.csv', 'test1.csv', 'test.csv')
    assert hasattr(vs, 'currencies')
    assert hasattr(vs, 'data')
    assert hasattr(vs, 'matching')

    assert type(vs.currencies) == dict
    assert type(vs.data) == list
    assert type(vs.matching) == dict


@pytest.fixture
def vs():
    return ValuationService('currencies.csv', 'data.csv', 'matchings.csv')


def test_calculate_total_price(vs):
    vs.calculate_total_price()
    total_prices = [x['total_price'] for x in vs.data]

    assert total_prices == [4800.0, 2205.0, 2000.0, 7350.0, 11760.0, 21000.0, 7560.0, 8400.0, 10080.0]


def test_filter_and_sort_products_matching_id(vs):
    vs.calculate_total_price()

    f_and_s_1 = vs.filter_and_sort_products_matching_id('1')
    f_and_s_1_total_prices = [x['total_price'] for x in f_and_s_1]
    assert f_and_s_1_total_prices == [10080.0, 2205.0, 2000.0]

    f_and_s_2 = vs.filter_and_sort_products_matching_id('2')
    f_and_s_2_total_prices = [x['total_price'] for x in f_and_s_2]
    assert f_and_s_2_total_prices == [21000.0, 7350.0]

    f_and_s_3 = vs.filter_and_sort_products_matching_id('3')
    f_and_s_3_total_prices = [x['total_price'] for x in f_and_s_3]
    assert f_and_s_3_total_prices == [11760.0, 8400.0, 7560.0, 4800.0]


def test_choose_n_best_products(vs):
    vs.calculate_total_price()
    f_and_s_1 = vs.filter_and_sort_products_matching_id('1')
    best_2_p = vs.choose_n_best_products(2, f_and_s_1)
    best_2_p_keys = list(best_2_p[0].keys())
    assert best_2_p_keys == ['avg_price', 'currency', 'ignored_products_count', 'matching_id',
                             'total_price']

    best_2_p_total_prices = [x['total_price'] for x in best_2_p]
    assert best_2_p_total_prices == [10080.0, 2205.0]


def test_run(vs):
    vs.run('test_output.csv')

    output_file_content = '''avg_price,currency,ignored_products_count,matching_id,total_price
                            4761.666666666667,GBP,1,1,10080.0
                            4761.666666666667,EU,1,1,2205.0
                            14175.0,PLN,0,2,21000.0
                            14175.0,EU,0,2,7350.0
                            8130.0,EU,1,3,11760.0
                            8130.0,EU,1,3,8400.0
                            8130.0,GBP,1,3,7560.0'''
    with open('test_output.csv', 'r') as file:
        for line in output_file_content.splitlines():
            assert file.readline().strip() == line.strip()
