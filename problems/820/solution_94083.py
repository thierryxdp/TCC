def posLetra(frase,letra,numero):
    indice=0
    tupla=tuple()
    while indice<len(frase):
        if letra in frase:
            tupla=tupla+(str.index(frase,letra),)
        indice=indice+1
    if numero>len(tupla):
        return -1
    else:
        return str.index(frase,tupla[numero])