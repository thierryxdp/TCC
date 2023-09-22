def eh_quadrada(M):
    for i in len(M):
        for j in len(M[0]):
            if M[i][j] == M[i][j]:
                return True
            else:
                return False