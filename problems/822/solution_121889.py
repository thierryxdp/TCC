def repetidos(lista):
    posicao = 1
    numero_de_repetidos = 0
    repeticao = (lista[posicao - 1] == lista[posicao])
    while posicao<len(lista):
             numero_de_repetidos = numero_de_repetidos + list.count(lista, lista[posicao - 1] == lista[posicao])
          posicao = posicao + 1
    return numero_de_repetidos