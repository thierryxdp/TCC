def eh_quadrada(m):
    if any(len(linha) != len(m) for linha in m):
        return False

    for i in range(len(m)):
        for j in range(i): 
            if m[i][j] != m[j][i]:
                return False
    return True