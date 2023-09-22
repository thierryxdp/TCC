import re
def conta_frases(texto):
    lista=re.split('[.!?]',texto)
    if'...'in texto:
        texto=texto.replace('...','!')
        return len(lista)