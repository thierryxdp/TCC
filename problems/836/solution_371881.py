def busca(setor,matriz):
    '''Função que dado um setor, busca todas as informações de todos os funcionários do setor;
    str, list -> list'''
    info = []
    for x in range(1,len(matriz)):
        if setor in matriz[x]:
            matriz[x].remove(setor)
        info = info + [matriz[x]]
    return matriz