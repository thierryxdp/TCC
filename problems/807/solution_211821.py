def conta_frases(frase):
    texto=frase.replace('!','0')
    texto=frase.replace('?', '0')
    texto=frase.replace('...','0')
    texto=frase.replace(',','0')
    return texto.split('0')