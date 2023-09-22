def eh_quadrada(M):
    if len(M) != len(M[0]):
        return False
    else:
        return True
    for i in range(len(M)):
        for j  in range(len(M[0])):
            if M[i][j] != M[i][j]:
                return False
     	return True