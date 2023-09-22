def repetidos(lista_num):
    posicao = 0
    repeticao = []
    while posicao < len(lista_num):
        if lista_num[posicao] == lista_num[posicao -1]:
            repeticao.append(1)
        posicao = posicao + 1
    return sum(repeticao)