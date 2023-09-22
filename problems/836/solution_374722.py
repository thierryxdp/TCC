def busca (setor, matriz):
    '''função que dada uma matriz e um setor devolve os dados de todos os funcionários daquele
    setor; str, list->list'''
    info = []
    for pessoa in matriz:
        if pessoa[2] == setor:
            info += [pessoa] 
    return info