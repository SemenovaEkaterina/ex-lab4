#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ["a", "A", 'B', 'b']
data4 = ["Nna", "nna", None]

# Реализация задания 2

for i in Unique(data1):
	print(i)
print()

for i in Unique(data2):
	print(i)
print()

for i in Unique(data3, ignore_case = True):
	print(i)
print()

for i in Unique(data4, ignore_case1 = True):
	print(i)
print()


for i in Unique(data4):
	print(i)
