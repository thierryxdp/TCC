def inverte(frase):
    for palavra in frase.split(" "):
        frase += palavra[::-1]+" "
        return frase