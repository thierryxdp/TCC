def busca(setor,matriz):
    '''Funcao que retorna os dados de todos os funcionários do setor
    de entrada.
    list,str->list'''
    x=0
    total=[]
    for x in range(len(matriz)):
        if s in matriz[x]:
            total=total+matriz[x]
        x=x+1
    return total