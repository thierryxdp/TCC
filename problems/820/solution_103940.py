def posLetra(frase,letra,posi):
    i=0
    posicao=0
    if posi>str.count(frase,letra):
        return -1
    while i<len(frase):
        if letra in frase[i]:
            posicao=posicao+1
        if posi==posicao:
            return i
        i=i+1