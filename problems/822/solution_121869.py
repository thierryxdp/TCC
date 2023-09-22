def repetidos(lista):
    posicao = 0
    numero_de_repetidos = 1
    repeticao = (lista[posicao - 1] == lista[posicao])
    while posicao<=len(lista):
          if repeticao>0:
             numero_de_repetidos = numero_de_repetidos + list.count(lista, repeticao)
          posição = posicao + 1
    return numero_de_repetidos