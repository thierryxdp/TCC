def inverte(frase):
    invertida = ' '.join(palavra[1::] for palavra in frase.split())
    return frase