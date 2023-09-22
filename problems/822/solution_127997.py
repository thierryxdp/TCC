def repetidos(x):
    '''
    list-> int
    '''
    y = 0
    i = 0
    while i < (len(x)-1):
        if x[i] == x[i+1]:
            y = y + 1
        i = i+1
    return y