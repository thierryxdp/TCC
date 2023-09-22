def busca (setor, matriz):
    '''função que dada uma matriz e um setor devolve os dados de todos os funcionários daquele
    setor; str, list->list'''
    info=[]
    for pessoa in matriz:
        for dado in pessoa:
            if dado[2]==setor:
                info+=pessoa
    return pessoa