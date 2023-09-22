def melhor_volta (matriz6x10):
    '''c'''
    resp=()
    for i in range(6):
        for j in range(10):
            resp+=(matriz6x10[i][j])
    return (i,min(resp),j)