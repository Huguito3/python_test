import re

class palindromo:
    def palindromo(palavra):
        palavra_reduzida=''
        for element in palavra.lower():
            if re.match("^[A-Za-z0-9]*$", element):
                palavra_reduzida+=element
        palavra_reverza = ''.join(reversed(palavra_reduzida))
        return palavra_reduzida == palavra_reverza