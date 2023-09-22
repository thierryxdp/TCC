def intercala(lista1,lista2):
    '''Função que dada duas listas de entrada, intercala as duas em uma só.
    '''
    lista1_2 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    return lista1_2