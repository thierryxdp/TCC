def posLetra(frase,letra,n):
    ''''''
    i = 0
    posicoes = []
    while i < len(frase):
        if frase[i] == letra:
            pos = str.find(frase,letra,i)
            posicoes += pos
        i = i + 1
    return posicoes[n]