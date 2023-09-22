def soma_h(n):
    ''' '''
    trecho=list(range(1,(n+1)))
    h=[]
    for i in trecho:
        result=(1/i)
        h=h+[result]
    return sum(h)