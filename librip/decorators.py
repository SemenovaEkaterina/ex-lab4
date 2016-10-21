
def print_result(func):
	def wrapper(*args):
		if len(args) == 0:
			result = func()
		else:
			result = func(*args)
		print(func.__name__)
		if type(result) == dict:
			for i in result.keys():
				print(i, " = ", result[i])
		elif type(result) == list:
			for i in result:
				print(i)
		elif type(result) == tuple:
			if len(result) == 1:
				print(result[0])
		else:
			print(result)
		return result
	return wrapper

