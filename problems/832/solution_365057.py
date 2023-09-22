def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if len(M) == len(M[0]):
                return True
            if M[i][j] != M[j][i]:
                return False
            if M[j] != M[j][i]:
	            return False
    return True