def soma_h(n):
    '''
    int -> float'''
    h=0
    for i in range(1,n+1):
        h+=1/i
    return round(h,2)