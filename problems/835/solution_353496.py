def melhor_volta (matriz6x10):
    '''c'''
    resp=(0,0,0)
    for i in range(7):
        for j in range(11):
            resp=(matriz6x10[i][j])
    return (i,min(resp),j)