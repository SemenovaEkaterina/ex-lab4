import random


# Генератор вычленения полей из массива словарей
def field(items, *args):
	assert len(args) > 0
	
	for n in items:
		if len(args) == 1:
			if not n.get(args[0]) is None:
				yield n.get(args[0]);
		else:
			new_items = {};
			for x in args:
				if not n.get(x) is None:
					new_items[x] = n[x]

			if len(new_items) > 0:
				yield new_items;



# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
	a = 0;
	while a < num_count:
		yield begin + round(random.random()*(end - begin))
		a += 1
		
