def faltante(lista):
    posicao = 0
    faltante = 0
    while posicao<len(lista):
          if sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista) != 0:
             faltante = sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista)
          posicao = posicao + 1
          if sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista) == 0:
            faltante = len(lista) + 1
    return faltante