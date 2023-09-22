def posicao():
    i = 0
    ocorrencias = 0
    while ocorrencias < numero:
        if letra in frase[i]:
            posicao = i
        i = i+1
    return posicao
def posLetra(frase,letra,numero):
    i = 0
    ocorrencias = 0
    while i<len(frase):
        if letra in frase[i]:
            ocorrencias = ocorrencias + 1
        if ocorrencias < numero:
            posicao = -1
        if ocorrencias >= numero:
            posicao = posicao()
        i = i+1
    return posicao