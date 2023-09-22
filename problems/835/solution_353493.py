def melhor_volta (matriz6x10):
    '''c'''
    resp=[]
    for i in range(7):
        for j in range(11):
            resp+=(matriz6x10[j])
    return (i,min(resp),j)