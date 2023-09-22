def busca(setor,matriz):
    '''Retorna os dados de todos os funcionarios de um setor dado uma matriz que possui quatro entradas'''
    y=[]
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                		matriz[i].remove(setor)
                	    y=y+[matriz[i]]
    return y