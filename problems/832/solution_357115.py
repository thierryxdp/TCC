def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas+1):
            if linhas == colunas:
                return True
            else: 
                return False