def repetidos(lista_num):
    '''função que dado uma lista de números, retorna quantas vezes um 
    elemento da lista é igual ao elemento anterior; list-->int'''
    proximo=0
    repete=0
    while proximo<len(lista_num):
        if lista_num[proximo]=lista_num[proximo+1]:
            repete=repete+1
        proximo=proximo+1
    return repete