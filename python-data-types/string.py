#declaring string
name = "hello"


#string indexing
print(name[0])
print(name[1])
print(name[-1])


#FORMATTED STRINGS
first = 'john'
last = 'smith'
msg = f'{first} [{last}] is a coder'
print(msg)

#STRING SLICING
# --simple example
print(name[1:3])
print(name[1:-1])
# -- slicing that have no starting index but have an ending index
print(name[:4])
# --slicing that have a starting index but not have an ending index
print(name[2:])
# --slicing tip to palindrome a string
print(name[::-1])


#STRING METHODS

print(name.capitalize()) #capitalise the first character of string
print(name.islower())  #check if there atleast one lowercase letter
print(name.isupper())  #che3ck if there is atleast one uppercase letter
print(name.isalpha())  #check if there is alphabetical character or not
print(name.isalnum())  #check i fthere are alphabet or numeric character in string
print(name.swapcase())  #swap the case of every character in string
print(name.find('h'))
print(name.find('O'))
print(name.replace('h','k'))
print(name.upper())
print(name.lower())
print('e' in name)
#LEN FUNTION
print(len(name)) #find the lenght of the strings

