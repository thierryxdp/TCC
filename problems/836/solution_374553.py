def busca(empregados,matriz):
    '''funcao que recebe uma string e matriz e busca o nome do empregado e retorna uma lista com os dados desse empregado
    str,list->list'''
    lista=[]
    for x in range(len(matriz)):
        if empregados==matriz[x]:
            lista=lista+[[matriz[x]]
    return lista