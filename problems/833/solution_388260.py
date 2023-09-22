def conta_numero(numero, matriz):
  linha = len(matriz[0][0])
  coluna = len(matriz[0])
    for numero in matriz:
        conta=list.count(numero(matriz))
    return conta