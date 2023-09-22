def media_matriz(A):
    soma = 0
	count=0
    media=0
    for i in  range(len(A)):
        for j in range(len(A[i])):
        	soma +=A [i][j]
			count+=1
	media=soma/count
	return media