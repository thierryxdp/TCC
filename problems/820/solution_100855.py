def posLetra(frase,letra,n):
    posicao=0
    while proximo < len(frase):
        if str.count(frase,letra)<n:
            return -1
        elif str.count(frase,letra)>=n:
            return str.index(frase,letra,n)