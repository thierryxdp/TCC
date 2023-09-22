import re
def conta_frases(texto):
    '''Separa as frases do parâmetro texto e retorna a sua quantidade
    str->int'''
    if '...'in texto:
        texto=texto.replace('...','!')
    return len(re.split('[.!?]',texto))-1