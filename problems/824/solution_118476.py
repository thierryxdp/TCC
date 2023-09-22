def uppCons(x):
    '''
    str->str
    '''
    y=[]
    w=0
    while w<len(x):
        if x[w] not in 'aeiouãóúíé':
            y= y+ [str.upper(x[w])]
        else:
            y= y+ [x[w]]
        w=w+1
    return str.join('',y)