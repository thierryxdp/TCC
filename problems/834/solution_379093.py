def media_matriz(a):
    soma=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            soma=soma+a[i][j]
            
     return soma/(len(a)*len(a[len(a))])