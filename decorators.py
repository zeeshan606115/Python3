auth_data = {
	"saud": 1234,
	"zeeshan": 435,
	"manas": 567
}
def authorized(func):

	def wrapper(username, password):
		if username in auth_data.keys():
			if password == auth_data[username]:
				return func()
		return "Not authorized"

	return wrapper

@authorized
def get_comments():
	return 'hello Comments'




# get_comment_with_auth = authorized(get_comments)
# print(get_comment_with_auth('zeeshan', 435))
print(get_comments('zeeshan', 435))

print(get_comments('zeeshan', 4353))