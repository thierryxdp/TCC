def repetidos(lista):
    posicao = 0
    numero_de_repetidos = 0
    while posicao<len(lista):
          numero_de_repetidos = numero_de_repetidos + list.count(sorted(lista), sorted(lista[posicao - 1]) == sorted(lista[posicao]))
          posicao = posicao + 1
    return numero_de_repetidos