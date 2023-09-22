def busca(setor,matriz):
    '''retorna os dados de todos do setor informado
    str,matriz->list'''
    a=[]
    for i in len(matriz):
        if setor in matriz[i]:
            matriz[i].pop(2)
            a+=[matriz[i]]
            
    return a