def media_matriz(a):
    soma=0
    d=len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            soma=soma+a[i][j]
	k=len(a[d-1])
    return soma/(k*d)