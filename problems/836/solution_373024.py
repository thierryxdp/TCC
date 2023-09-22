def busca(s,m):
    '''Recebe um setor(s) e uma matriz(m),
    Retorna os dados de todos os funcionários daquele setor.
    str,list->list'''
    x=[]
    for i in m:
        for j in i:
            if j==s:
                list.remove(i,j)
                list.append(x,i)
    return x