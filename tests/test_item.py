"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
def test_name_setter():
    item1 = Item('Телефон', 10000, 5)
    item2 = Item('Ноутбук', 10000, 5)
    item1.name = 'Смартфон'
    item2.name = 'Ультраноутбук'
    assert item1.name == 'Смартфон'
    assert item2.name == 'Ультраноут'
def test_string_to_number():
    assert Item.string_to_number('5') == 5

def test_total_price():
    item = Item('Ноутбук', 10000, 5)
    assert Item.calculate_total_price(item) == 50000

def test_discount():
    Item.pay_rate = 0.5
    item = Item('Телефон', 18000, 5)
    Item.apply_discount(item)
    assert item.price == 9000

def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5