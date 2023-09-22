def busca(setor,matriz):
    ''' função que retorna os dados dos funcionários de um detrminado setor, dada como parãmetro uma matriz que apresente esses dados 
    str, list --> list'''
    x = []
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                		matriz[i].remove(setor)
                	    x = x+[matriz[i]]
    return x