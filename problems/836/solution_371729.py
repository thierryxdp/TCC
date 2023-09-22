def busca(st,m):
    '''busca funcionarios e suas informações r'''
    func=[]
    for i in range(len(m)):
        if st in m[i]:
            m[i].remove(st)
            y =[m[i]]
    return y