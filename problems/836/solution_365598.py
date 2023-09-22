def busca(setor,m):
    '''retorna os dados dos funcionarios do setor em questão
    str,list->list'''
    i=0
    for setor in m:
        if m[i][2]==setor:
            i=i+1
            return m[i]-m[i][2]
        else:
            return []