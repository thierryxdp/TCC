def busca(setor, matriz):
    '''Recebe uma string(setor) e uma lista(matriz), faz uma 
    busca por setor e devolve uma outra lista(lista_retorno)
    com os dados de todos os funcionários daquele setor.'''
    #Lista de retorno
    lista_retorno=[]
    #Percorre a matriz enquanto i estiver nela
    for i in matriz:
        if i[2]==setor:
            #para não incluir o setor na lista.
            lista_retorno.apprnfr(i[0:2]+i[3:])
    return lista_retorno