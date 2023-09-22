def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M == []:
                return True
            if  M[i][j] != M[j][i]:
                return False
            if len(M[0]) == len(M):
                return True
            else:
                return False