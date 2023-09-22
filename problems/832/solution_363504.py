def eh_quadrada(matriz):
    linha = 0
    coluna = 0
    
    for i in range(len(matriz)):
        linha = linha +1
    
    for j in range(i):
        coluna = coluna + 1
    
    if coluna == linha:
        return True
    else:
        return False