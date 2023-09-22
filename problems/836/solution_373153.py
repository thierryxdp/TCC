def busca(setor,matriz):
    '''função que dado o setor de uma empresa e uma matriz contendo as informações dos funcionários retorna a lista contendo as informações dos empregados que trabalham naquele ramo; setor, matriz>>lista'''
    for c in matriz:
        for i in c:
            e= c[2]
            if setor in e:
                return i
    return []