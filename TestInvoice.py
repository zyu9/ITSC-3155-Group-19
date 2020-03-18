import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(products):
    invoice = Invoice()
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(products):
    invoice = Invoice()
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateExtraDiscount(products):
    invoice = Invoice()
    invoice.extraDiscount(products)
    assert invoice.extraDiscount(products) == 5

def test_CanCalculateTotalFinalPrice(products):
    invoice = Invoice()
    invoice.totalFinalPrice(products)
    assert invoice.totalFinalPrice(products) == 64.38
