def eh_quadrada(matriz):
   """
   função que indentifica se a matriz é quadrda
   """
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
             return True 
        else:
             return False