def busca(setor, matriz):
    '''Função que dada uma matriz e um setor da empresa, realiza uma busca e
    retorna as informações dos funcionários que pertencem ao setor. 
    list, str -> list'''
    for i in matriz:
        if setor in matriz[i]:
            x = list.remove(matriz[i], setor)
            return x
        else:
            return []