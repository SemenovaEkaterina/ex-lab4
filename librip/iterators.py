# Итератор для удаления дубликатов
class Unique(object):
	def __init__(self, items, **kwargs):
        


		
		self.ignore_case = kwargs.get('ignore_case', False)


		
		self.items = iter(items)

		self.unique_items = set()


		self.index = 0
	

	def __next__(self):


		for x in self.items:
			if not x is None:
				origin = x
				if self.ignore_case == True:
					x = str(x).lower()
				if not x in self.unique_items:
					self.unique_items.add(x)
					return origin
		
		raise StopIteration

	def __iter__(self):
		return self
