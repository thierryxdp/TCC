def busca(setor,matriz):
    '''Função que dado um setor, busca todas as informações de todos os funcionários do setor;
    str, list -> list'''
    for x in range(1,matriz+1):
        if setor in matriz[x]:
            matriz[i].remove(setor)
    return matriz