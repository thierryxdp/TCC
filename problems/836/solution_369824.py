def busca(setor,matriz):
    '''Funcao que retorna os dados de todos os funcionários do setor
    de entrada.
    str,list->list'''
    x=0
    total=[]
    for x in range(len(matriz)):
        if setor in matriz[x]:
            del matriz[x][2]
            total=total+[matriz[x]]
        x=x+1
    return total