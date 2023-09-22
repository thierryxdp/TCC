def busca(string,matriz):
    '''retorna os dados de todos os funcionarios de um setor
    str,list->list'''
    
    setor=[]
    
    for l in range(len(matriz)):
        if string == matriz[l][2]:
            setor+=[[matriz[l][0],matriz[l][1],matriz[l][3],]]
    return setor