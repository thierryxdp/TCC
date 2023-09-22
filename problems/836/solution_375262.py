def busca(s,m):
    '''Função que recebe uma matriz e busca pelo setor, dado como entrada a matriz e o setor; str->list'''
    r=[]
    for linha in range(len(m)):
        if s==m[linha][2]:
            list.remove(m[linha],s)
            list.append(r,m[linha])
    return r