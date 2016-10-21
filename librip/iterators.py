# Итератор для удаления дубликатов
class Unique(object):
	def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        
		if len(kwargs) != 0:
			self.ignore_case = kwargs['ignore_case']
		else:
			self.ignore_case = kwargs['ignore_case'] = False

		self.items = items

		self.unique_items = []


		self.index = 0
	

	def __next__(self):

		if type(self.items) == list:
			self.items = iter(self.items)

		for x in self.items:
			if not x is None:
				origin = x
				if self.ignore_case == True:
					x = str(x).lower()
				if not x in self.unique_items:
					self.unique_items.append(x)
					return origin
		
		raise StopIteration

	def __iter__(self):
		return self
