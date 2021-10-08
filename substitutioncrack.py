import itertools
import time
import sys

file = sys.argv[1]

original_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
subst_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']

def getnletwords(n, arr):
	narr = []
	for word in arr:
		if len(word) == n:
			narr.append(word)
	nletdict = {}
	for word in narr:
		if word in nletdict:
			nletdict[word] += 1
		else:
			nletdict[word] = 1
	return nletdict

def printnwords(arr):
	one_let = getnletwords(1, arr)
	two_let = getnletwords(2, arr)
	three_let = getnletwords(3, arr)
	four_let = getnletwords(4, arr)
	five_let = getnletwords(5, arr)
	six_let = getnletwords(6, arr)
	print(one_let)
	print(two_let)
	print(three_let)
	print(four_let)
	print(five_let)
	print(six_let)
	print()

def substitute(cipher_text, subst_dict):
	plain_text = ''
	for c in cipher_text:
		if c in subst_dict:
			plain_text += subst_dict[c]
		else:
			plain_text += c
	return plain_text

def make_dict(c_arr, o_arr):
	subst_dict = {}
	for i in range(len(c_arr)):
		subst_dict[c_arr[i]] = o_arr[i]
	return subst_dict

if file == 'cipher1.txt':
	f = open('cipher1.txt', 'r')
	cipher_text = f.readline()

	print(cipher_text)
	print()
	printnwords(cipher_text.split())

	c_arr = ['v']
	o_arr = ['a']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9']
	o_arr = ['a', 't', 'h', 'e']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9', '@', 'o']
	o_arr = ['a', 't', 'h', 'e', 'n', 'd']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9', '$', 'p', '1', '@', '8']
	o_arr = ['a', 't', 'h', 'e', 'o', 'f', 'b', 'n', 'd']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9', '$', 'p', '1', '@', '8', '#', '5', 'y', 's', 't']
	o_arr = ['a', 't', 'h', 'e', 'o', 'f', 'b', 'n', 'd', 'w', 'i', 's', 'u', 'c']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9', '$', 'p', '1', '@', '8', '#', '5', 'y', 's', 't', '2', '6', '7', 'u']
	o_arr = ['a', 't', 'h', 'e', 'o', 'f', 'b', 'n', 'd', 'w', 'i', 's', 'u', 'c', 'r', 'v', 'g', 'l']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['v', 'o', 'q', '9', '$', 'p', '1', '@', '8', '#', '5', 'y', 's', 't', '2', '6', '7', 'u', '0', '3', '4', 'x', 'w', 'r']
	o_arr = ['a', 't', 'h', 'e', 'o', 'f', 'b', 'n', 'd', 'w', 'i', 's', 'u', 'c', 'r', 'v', 'g', 'l', 'm', 'p', 'q', 'y', 'k', 'x']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	print('Decrypted Text')
	print()
	print(plain_text)

elif file == 'cipher2.txt':
	f = open('cipher2.txt', 'r')
	cipher_text = f.readline()

	print(cipher_text)
	print()
	printnwords(cipher_text.split())

	c_arr = ['1']
	o_arr = ['a']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q']
	o_arr = ['a', 'h', 'e']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q', '4', 'v']
	o_arr = ['a', 'h', 'e', 'l', 's']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q', '4', 'v', 'r', '8', '@', 't']
	o_arr = ['a', 'h', 'e', 'l', 's', 'i', 'p', 't', 'r']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q', '4', 'v', 'r', '8', '@', 't', 'z', 'y', '5', 'p']
	o_arr = ['a', 'h', 'e', 'l', 's', 'i', 'p', 't', 'r', 'd', 'n', 'w', 'g']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q', '4', 'v', 'r', '8', '@', 't', 'z', 'y', '5', 'p', '$', '9', '7', '#']
	o_arr = ['a', 'h', 'e', 'l', 's', 'i', 'p', 't', 'r', 'd', 'n', 'w', 'g', 'o', 'v', 'b', 'u']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	c_arr = ['1', 'n', 'q', '4', 'v', 'r', '8', '@', 't', 'z', 'y', '5', 'p', '$', '9', '7', '#', '3', 's', '2', 'w', '6', 'x']
	o_arr = ['a', 'h', 'e', 'l', 's', 'i', 'p', 't', 'r', 'd', 'n', 'w', 'g', 'o', 'v', 'b', 'u', 'c', 'm', 'y', 'f', 'k', 'j']
	plain_text = substitute(cipher_text, make_dict(c_arr, o_arr))
	print(plain_text)
	print()
	printnwords(plain_text.split())

	print('Decrypted Text')
	print()
	print(plain_text)

else:
	print('File should be cipher1.txt or cipher2.txt')