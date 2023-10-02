# # Screen output
# first_name: str = "Fred"
# print(first_name)
#
# # Extend a string
# first_name = "Fred" + " " "O'Connor"
# print(first_name)
#
# # Re-assigning "int" type to a previously declared "str" type
# # Python allows this as it is a dynamically typed language
# first_name: int = 1
# print(first_name)
#
# # Initializing variables
# my_first_int: int = 3
# print(my_first_int)
#
# # Exploring backslash
# # Screen output
# first_name: str = "Fred \\ \n"
# print(first_name)
#
# # Exploring f-string
# print(f'The first integer is: {my_first_int}')

# str1 = 'xyz123'
# strlen = len(str1) # 'len()' is a built-in function
# print(strlen)
#
# # Exploring string positions
# str1 = 'abcdef'
# print(str1[0], str1[1])
#
# # Exploring range
# str1 = 'abcdefghi'
# print(str1[2:6])
#
# str1 = 'abcdefghijklmno'
# print(str1[3:11:2])

# immutable: str, int, float, tuple
# mutable: list

# Getting input from the user
#prompt: str = 'What is your name? '
#resp = input(prompt)
#print(resp)

# str = 'abcdefghi'
# last = str[-1]
# print(last)
# print(str[-2])

# str = 'abcdefghi'
# print(str[2:-2])
# print(str[::-2])
# print(str[::2])

# str = 'abcdefghi'
# print(str[-4:-2])
#
# bigstr = 'abc' * 3
# print(bigstr)
# divider = '=' * 30
# print(divider)

# bigstr5 = 'First Name\t Last Name'
# print(bigstr5)

# str1 = """Hello everybody
# this is a long string that
# takes up multiple lines!
# We use triple-quotes for it!"""
# print(str1)

# str1 = r'I need a backslash\in this string. And the \t does not make a tab!'
# print(str1)

# Example of replacing a string
favorite_color = 'Red!'
print(favorite_color)
favorite_color = 'Blue!'
print(favorite_color)

str = 'hello'
print(str + ' world')
str = str + "yay it worked"
print(str)