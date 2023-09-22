def posLetra(frase,letra,numero):
    i = 0 
    posicao = 0 
    ocorrencias = 0
    while i < len(frase):
        if letra in frase[i]:
            ocorrencias = ocorrencias + 1
        if ocorrencias < numero:
            posicao = -1
        if ocorrencias > numero: 
            while ocorrencias >= numero: 
                if ocorrencias >= numero:
                    posicao = posicao + 1
        i = i+1
    return posicao