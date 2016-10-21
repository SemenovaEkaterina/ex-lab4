
# контекстный менеджер timer
import time

class timer:
	def __enter__(self):
		self.t = time.time()
	def __exit__(self, exp_type, exp_value, traceback):
		print(time.time() - self.t)

