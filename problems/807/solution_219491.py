import re
def conta_frases(texto):
    lista=re.split('[.!?]',texto)
    if'...'in texto:
        return texto.replace('...','!')
    return len(lista)