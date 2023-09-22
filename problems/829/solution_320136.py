def soma_h(N):
    '''int->float'''
    H=1
    i=1
    list(range(1,N+1))
    for i in list(range(1,N+1)):
        H=1+(1/i+1)
        i=i+1
    return H