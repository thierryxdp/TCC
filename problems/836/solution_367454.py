def busca(setor,matriz):
    '''dado um numero de setor e uma matriz com listas de informações referentes a funcionários, retorna os dados dos funcionários do setor informado
    str,list-->list'''
    dados=[]
    for i in matriz:
        if setor in i:
            dados+=[i[0],i[1],i[3]]
    return dados