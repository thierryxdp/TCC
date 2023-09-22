def busca(setor,matriz):
    '''funcao que recebe uma string e uma matriz e faz uma busca por setor e
    retorna uma lista com os dados de todos os funcionarios daquele setor
    string, list -> list'''
    lista = [ ]
    for i in matriz:
        listaA = [ ]
        if setor in i[2]:
            listaA = listaA + [i[0]] + [i[1]] + [i[3]]
            lista = lista + [listaA]
    return lista