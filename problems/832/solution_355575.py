def eh_quadrada(m):
    for i in range(len(m)):
        for j  in range(len(m[0])):
            if m[i][j] != m[j][i]:
                return False
    return True