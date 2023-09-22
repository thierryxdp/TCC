def inverte(frase):
    x=str.split(frase," ")
    invertida = ' '.join(x[::-1] for palavra in frase.split())
    return invertida