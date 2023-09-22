def busca(setor,matriz):
    '''Dados um setor e uma matriz com os dados dos
    funcionários de uma empresa, retorna os contatos dos
    funcionários do setor.
    str, list -> list'''
    retorno=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            retorno=retorno+[matriz[i]]
    return retorno