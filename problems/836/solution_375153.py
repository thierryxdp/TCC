def busca(setor,matriz):
    '''Função que recebe uma string e uma matriz e faz uma busca por setor, 
    retornando  uma lista com os dados de todos os funcionários daquele setor;
    string, list -> list'''
    
    lista = [ ]
    for i in matriz:
        listaA = [ ]
        if setor in i[2]:
            listaA = listaA + [i[0]] + [i[1]] + [i[3]]
            lista = lista + [listaA]
    return lista