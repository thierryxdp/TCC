def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in linhas:
        for j in colunas:
            if i == j:
                return True
            else: 
                return False