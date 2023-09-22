def busca(setor,matriz):
    '''Dada uma matriz e um setor retorna o dado de todos os funcionários deste setor
    list,str -> list'''
    lista = []
    for i in matriz:
        if setor in i:
            lista.append(i[0:2] + [i[3]]) 
    return lista