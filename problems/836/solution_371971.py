def busca(setor,matriz):
    """ recebe uma matriz e retorna os dados de todos os
    funcionarios daquele setor.
    str,list-->list"""
    y=[]
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                		matriz[i].remove(setor)
                	    y=y+[matriz[i]]
    return y