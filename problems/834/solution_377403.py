def media_matriz(x):
    '''Entre com uma matriz para ser retornado seu valor medio
    Matriz-> Float'''

    soma=0
    count=0
    
    n_lin= len(x)
    if n_lin==0:
        return 0
    n_col=len(x[0])

    for i in range(n_lin):
        soma=soma+x[i]
        count=count+1
        for j in range(n_col):
            soma=soma+x[i][j]
            count=count+1

    div=soma/count
    return round(div,2)