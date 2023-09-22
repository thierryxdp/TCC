def media_matriz(A):
    count = 0
	soma=0
    for i in  range(len(A)):
        for j in range(len(A[i])):
        	if A [i][j] == n:
            	cont += 1
    for i in  range(len(A)):
        for j in range(len(A[i])):
        	soma+= A [i][j]
	media=soma/count
	return media