def busca(setor, m):
    ''' Retorna todos os dados dos funcionarios de um dado setor'''
    l = []
    for e in m:
        if setor in e:
            l.append(e)
    return l