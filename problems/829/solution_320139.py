def soma_h(N):
    '''int->float'''
    i=0
    list(range(1,N))
    for i in list(range(1,N)):
        H=1+(1/(i+1))
        i=i+1
    return round(H,2)