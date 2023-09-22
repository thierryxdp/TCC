def repetidos(lista):
    posicao = 0 
    numero_de_repetidos = 0
    while posicao<len(lista) - 1:
          numero_de_repetidos = numero_de_repetidos + list.count(lista[::1],lista[posicao] == lista[posicao + 1])
          posicao = posicao + 1
    return numero_de_repetidos