def inverte(frase):
    x=str.split(frase," ")
    invertida = ' '.join(palavra[::-1] for palavra in x.split())
    return invertida