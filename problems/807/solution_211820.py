def conta_frases(frase):
    texto=frase.replace('!','0')
    texto=frase.replace('?', '0')
    texto=frase.replace('...','0')
    texto=frase.replace(',','0')
    print(texto.split('0'))