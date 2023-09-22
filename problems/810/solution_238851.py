import re

def inverte(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

frase = 'Oi, tudo bem?     Blablabla'
invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\W+)', frase))
print(invertida)