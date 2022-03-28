def fun_1():
    'this is a function'

def fun_2():
    #this is another function
    exit

#USING DOC ATTRIBUTE FOR ACCESSING DOCSTRING  
print(fun_1.__doc__)

#USING DOC ATTRIBUTE WITH COMMENTS 
print(fun_2.__doc__)

#USING GOOGLE STYLE PYTHON
def hello(name, language="english"):
 """Say hello to a person.
 Args:
 name: the name of the person as string
 language: the language code string
 Returns:
 A number.
 """
 print(name + ' in ' + language)
 return 4
hello('chirag','english language')
