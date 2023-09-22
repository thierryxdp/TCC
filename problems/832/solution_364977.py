def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if  M[i][j] != M[j][i]:
                return False
            elif M[i][j] == M[j][i]:
                return True
            else:
                return False
        return False