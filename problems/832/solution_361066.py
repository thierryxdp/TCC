def eh_quadrada(matriz):
    if matriz==[]:
        return True
    Colunas=len(matriz[0])
    Linhas=len(matriz)
    
    if Linhas == Colunas:
        return True
    else:
        return False