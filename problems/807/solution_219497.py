import re
def conta_frases(texto):
    if '...'in texto:
        texto=texto.replace('...','!')
        return len(re.split('[.!?]',texto))-1