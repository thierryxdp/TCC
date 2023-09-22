def soma_h(N):
    '''int->float'''
    lista=[]
    i=1
    list(range(1,N+1))
    for i in list(range(1,N+1)):
        list.append(lista,(1/i))
        i=i+1
    H=sum(lista)
    return round(H,2)