def intercala(lista1, lista2):
    '''Dado duas listas(lista1 e lista2) de tamanho 3, gera uma lista3 intercalando os elementos da lista1 e lista2
    list, list -> list'''
    # criando uma lista cujos elementos sao os da lista1 e lista2 intercalados, respectivamente.
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3