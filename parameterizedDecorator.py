
def prettify(symbol):

	def decorator(func):
		def wrapper(text):
			print(symbol*len(text))
			func(text)
			print(symbol*len(text))

		return wrapper
	return decorator


@prettify('=')
def print_city(city):
	print(city)

@prettify('*')
def print_country(country):
	print(country)

print_city('Ranchi')
print_country('India')



