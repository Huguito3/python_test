import re
from palindromo import palindromo
# def palindromo(palavra):
#     palavra_reduzida=''
#     for element in palavra:
#         if re.match("^[A-Za-z0-9]*$", element):
#             palavra_reduzida+=element
#     palavra_reverza = ''.join(reversed(palavra_reduzida))
#     return palavra_reduzida == palavra_reverza
    
pal = input("Ingrese a palavra: ").lower()
if palindromo.palindromo(pal) :
    print('É palindromo')
else:
    print('Não é palindromo')


# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    
    
