def busca(s,m):
    '''funçao que recebe uma matriz e faz uma busca por setor e 
    retorna os dados de todos funcionarios do mesmo; str->list'''
    n=0
    for l in range(len(m)):
        if s==m[l][2]:
            list.remove(m[l],s)
            list.append(n,m[l])
    return n