def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != M[j][i] or M[j] != M[j][i]:
                return False
            if len(M) == len(M[0]):
                return True
    return True