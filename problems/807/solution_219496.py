import re
def conta_frases(texto):
    if '...'in texto:
        texto=texto.replace('...','!')
        lista=re.split('[.!?]',texto)
        return len(lista)-1