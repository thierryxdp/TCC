import re
def conta_frases(texto):
    '''Função que, dado um texto qualquer, calcula o número de frases do texto.
str --> int'''
    if '...' in texto:
        return len(re.split('[.?!]',texto))-3
    if '...' not in texto:
        return len(re.split('[.?!]',texto))-1