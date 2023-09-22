def media_matriz(x):
    '''
    list->float 
    '''
    s=0
    for n in range(len(x)):
        m=x[n]
        for k in range(len(m)):
            s=s+m[k]
    med=(s/(len(x)*len(x[0])))        
    return round(med,2)