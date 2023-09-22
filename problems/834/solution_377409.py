def media_matriz(x):
    '''Entre com uma matriz para ser retornado seu valor medio
    Matriz-> Float'''

    soma=[]
    count=0
    
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        y=x[i]
        soma+=y
        count=count+1
        for j in range(n_col):
            y=x[i][j]
            soma+=y
            count=count+1

    div=soma/count
    return round(div,2)