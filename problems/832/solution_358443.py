def eh_quadrada(x):
    '''Entre com uma matriz para saber se ela e quadrada ou não
    Matriz -> Bool'''

    Pos_x=0
    Pos_y=0

    n_lin= len(x)
    n_col=len(m[0])
    
    for i in range(n_lin):
        Pos_x=Pos_x+1
        Pos_y=0
        for j in range(n_col):
            Pos_y=Pos_y+1

    multi=Pos_x*Pos_y

    if multi%2==0:
        return True
    else:
        return False