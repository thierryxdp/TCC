def eh_quadrada(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
    	if M[i][j] != M[i][j]:
   			return False
    else:
        return True