# implement simple hash table
# using int, float, array, pointer (which doesn't exist concretely in Python)

from string import ascii_lowercase

values = [None for i in range(100)] # bc i have to specify the size of the array first, and technically it can't grow

def hash_fn(key):
	if key[0] in ascii_lowercase:
		return ascii_lowercase.index(key[0])

assert hash_fn('a') == 0
assert hash_fn('b') == 1
assert hash_fn('y') > 20

def put_into_dict(word):
	word = word.lower()
	values[hash_fn(word)] = word

put_into_dict('games')
put_into_dict('same')
put_into_dict('xylophone')
put_into_dict('alpha')

assert values[0] == 'alpha'
assert values[6] == 'games'
assert values[18] == 'same'
assert values[23] == 'xylophone'

print values[:10]

# our version of collision here is the value in the array being overwritten