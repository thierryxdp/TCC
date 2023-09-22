def repetidos(lista):
    posição = 0
    número_de_repetidos = 1
    repetição = (lista[posição - 1] == lista[posição])
    while posição<=len(lista):
          if repetição>0:
             número_de_repetidos = número_de_repetidos + list.count(lista, repetição)
          posição = posição + 1
    return número_de_repetidos