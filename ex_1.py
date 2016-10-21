#!/usr/bin/env python3
from librip.gen import field
from librip.gen import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]


for x in field(goods, 'title'):
	print(x)


for x in field(goods, 'title1', 'price1'):
	print(x)

for x in field(goods, 'title', 'price', 'color'):
	print(x)



for x in gen_random(3, 5, 20):
	print(x)
