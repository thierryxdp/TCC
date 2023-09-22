def repetidos(lista):
    posicao = 0
    numero_de_repetidos = 0
    repeticao = (lista[posicao - 1] == lista[posicao])
    while posicao<=len(lista):
             numero_de_repetidos = list.count(lista, repeticao)
             posicao = posicao + 1
    return numero_de_repetidos