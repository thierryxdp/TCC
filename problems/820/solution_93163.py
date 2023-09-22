def posLetra(frase,letra,numero):
    i = 0
    ocorrencias = 0
    while i<len(frase):
        if letra in frase[i]:
            ocorrencias = ocorrencias + 1
        i = i+1
        while ocorrencias < numero:
            if letra in frase[i]:
                posicao = i
            i = i+1
        return posicao