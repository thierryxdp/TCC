def soma_h(n):
    '''
    int ---> float
    '''
    s = 0
    for i in range(1,n+1):
        s+=1/i
    return round(s,2)