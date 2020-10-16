from re import search
class Auth:
	@staticmethod
	def valid_password(password):
		return len(password) > 8 and search("[a-z]", password) != None and search("[A-Z]", password) != None and search("[0-9]", password) != None
