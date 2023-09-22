def eh_quadrada(m):
    for i, linha in enumerate(m):
        if len(linha) != len(m): 
            return False 
        for j in range(i):
            if linha[j] != m[j][i]:
                return False
    return True