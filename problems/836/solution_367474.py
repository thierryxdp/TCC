def busca(setor, matriz):
    '''Função que dada uma matriz e um setor da empresa, realiza uma busca e
    retorna as informações dos funcionários que pertencem ao setor. 
    list, str -> list'''
    lista = []
    i = 0
    while i <= len(matriz):
        if setor in matriz[i]:
            lista += [list.remove(matriz[i], setor), ]
        i = i + 1
    return lista