def conta_frases(frase):
    texto=frase.replace('!','X')
    texto=frase.replace('?', 'X')
    texto=frase.replace('...','X')
    texto=frase.replace(',','X')
    return texto.split('X')