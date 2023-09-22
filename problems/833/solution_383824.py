def conta_numero(num,x):
    '''Entre com um numero e uma matriz para saber quantas vezes esse numero
    se repete
    Matriz -> Int'''
    count=0
    
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        y = n_lin(i)
        if y == num:
            count=count+1
        for j in range(n_col):
            y = n_lin(i[j])
            if y == num:
                count=count+1
    return count