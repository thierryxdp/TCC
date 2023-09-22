def busca(funcao,matriz):
    '''busca recebe uma string e uma matriz e devolve uma lista
    determine uma lista que tenha os dados de uma pessoa, mas sem
    a funcao que ela realiza
    str, list(list) --> list'''
    
    lista = []
    
    for i in range(0,3):
        if funcao in matriz[i]:
            del matriz[i][2]
            list.append(lista,matriz[i])
        
    return lista