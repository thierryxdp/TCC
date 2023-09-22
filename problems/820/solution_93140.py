def posLetra(frase,letra,numero):
    i = 0 
    posicao = 0 
    ocorrencias = 0
    while i < len(frase):
        if letra in frase[i]:
            ocorrencias = ocorrencias + 1
        i = i+1
    while numero <= ocorrencias:
        if numero <= ocorrencias: 
            posicao = posicao + 1
        i = i+1
    return posicao