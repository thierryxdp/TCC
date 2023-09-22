def busca(st,m):
    '''busca funcionarios e suas informações baseadas em setor(st)'''
    r1 = []
    z=0
    for i in range(len(m)):
        if st in m[i]:
            r1 = r1 + [m[i]]
            r1[z].remove(st)
            z = z + 1
    return r1