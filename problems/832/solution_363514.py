def eh_quadrada(matriz):
    linha = 0
    coluna = 0
    
    matriz == []:
        return True
    
    for i in range(len(matriz)):
        linha = linha +1
    
    for j in range(i):
        coluna = coluna + 1
    
    if linha == coluna:
        return True
    else:
        return False