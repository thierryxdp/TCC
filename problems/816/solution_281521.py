def maiores(lista,n):
    '''
    retorna uma lista c os numeros maiores q m
    '''
     m=list()
    for h in lista:
        if h>=n:
            m.append(h)
            list.sort(m)
    return m