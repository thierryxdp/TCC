def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M[0]*M)):
            if  M[i][j] != M[j][i]:
                return False
        return True