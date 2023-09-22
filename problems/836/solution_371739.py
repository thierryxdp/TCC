def busca(st,m):
    '''busca funcionarios e suas informações r'''
    r1 = []
    for i in range(len(m)):
        if st in m[i]:
            r1 = r1 + [m[i]]
    return r1