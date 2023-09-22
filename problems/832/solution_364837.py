def eh_quadrada(matriz):
    if len(matriz) == 1 and len(matriz[0]) == 0:
        return True
  
    return all(len(matriz) == len(linha) for linha in matriz)