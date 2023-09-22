def faltante(lista):
    posicao = 0
    faltante = 0
    while posicao<len(lista):
          if (list(range(lista[len(lista) -1]))[posicao] - list(range(lista[len(lista) -1]))[posicao - 1]) != 1:
             faltante += list(range(lista[len(lista -1)])[posicao - 1]) 
          posicao = posicao + 1
    return faltante