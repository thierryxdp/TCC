def melhor_volta(x):
    '''Entre com uma matriz no formato 6x10 e nela contendo o tempo de cada
    volta
    Matriz -> Tupla'''

    npilot=0
    mtempo=800
    nvolta=0
    result=()
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        for j in range(n_col):
            y=x[i][j]
            if y<mtempo:
                mtempo=y

    return mtempo