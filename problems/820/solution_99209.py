def posLetra(frase,letra,n):
    ''''''
    i = 0
    posicao = []
    while i < len(frase):
        if frase[i] == letra:
            pos = str.find(frase,letra,i)
            posicao += [pos,]
        i = i + 1
    if len(posicao)<n:
        return -1
    else:
        return posicao[n-1]