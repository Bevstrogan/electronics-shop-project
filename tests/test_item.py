"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

product = Item('Часы Xiaomi', 4500, 18)
Item.pay_rate = 0.5
def test_price():
    assert Item.calculate_total_price(product) == 81000

def test_discount():
    assert Item.apply_discount(product) == 2250