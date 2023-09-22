def faltante(lista):
    posicao = 0
    faltantes = 0
    while posicao<len(lista):
          if list(range(lista[len(lista)]))[posicao] - list(range(lista[len(lista)]))[posicao - 1] != 1:
             faltante = list(range(lista[len(lista)])[posicao - 1]) + 1
          posicao = posicao + 1
    return faltante