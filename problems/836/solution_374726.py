def busca (setor, matriz):
    '''função que dada uma matriz e um setor devolve os dados de todos os funcionários daquele
    setor; str, list->list'''
    a=[]
    info = []
    for pessoa in matriz:
        if pessoa[2] == setor:
            info += [pessoa,] 
    for elem in info:
        b = list.append(a,[elem[0]]+[elem[1]]+[elem[3]])
    return b