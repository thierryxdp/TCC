def total(x,y):
    '''
    list,dict->float 
    '''
    z=0
    i=0
    
    while i<len(x):
        if x[i] in dict.keys(y):
            z=z+dict.get(y,x[i])
        i=i+1
    return round(z,2)