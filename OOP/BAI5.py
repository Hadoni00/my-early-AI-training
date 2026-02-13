from abc import ABC,abstractmethod
class ConVat(ABC):
	def __init(self,ten,tuoi,can_nang):
		self.ten = ten
		self._tuoi = tuoi 
		self.__can_nang = can_nang 
	@abstractmethod
	def keu():
		pass
	def an():
		print("Con vat dang an")
	def get():
		return __can_nang
class Cho(ConVat):
	def keu():
		print("Gau Gau")

class Meo(ConVat):
	def keu():
		print("Meo Meo")
class Vit(ConVat):
	def keu():
		print("Cap Cap")
ds = [Cho,Meo,Vit]
for i in ds:
	i.keu()
