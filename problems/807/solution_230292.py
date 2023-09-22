import re
def conta_frases(frase):
    delimitadores = frase.replace('...','!','?')
    return len(delimitadores.split('! '))