def soma_h(N):
    '''c'''
    resp=0
    for i in range(1,N+1):
        if N!=0:
            resp+=(1/i)
    return round(resp,2)