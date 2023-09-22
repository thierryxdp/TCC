def busca(st,m):
    '''busca funcionarios e suas informações r'''
    r1 = []
    if st in m[0]:
        r1 = r1 + m[0]
        r1[0].remove(st)
    if st in m[1]:
        r1 = r1 + m[1]
        r1[0].remove(st)
    if st in m[2]:
        r1 = r1 + m[2]
        r1[1].remove(st)
    return r1