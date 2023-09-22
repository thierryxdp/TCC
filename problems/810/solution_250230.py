import math

def retira_pontuacao(frase):
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if ':' in frase:
        frase = frase.replace(':', ' ')
    if '.' in frase:
        frase = frase.replace('.', ' ')
    if '!' in frase:
        frase = frase.replace('!', ' ')
    if '?' in frase:
        frase = frase.replace('?', ' ')
    return frase



def inverte(frase):
    
    frase = frase.lower()    
    frase = retira_pontuacao(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    x = ', '.join(frase)
    
    
    return x