def busca(setor,m):
    '''retorna os dados dos funcionarios do setor em questão
    str,list->list'''
    i=0
    for setor in m:
        if setor in m[i][2]:
            return m[i]-m[i][2]
        i=i+1
    else:
            return []