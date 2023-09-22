def faltante(lista):
    '''função que a partir de uma lista de números inteiros fornece o número que está faltando para essa lista ser crescente de 1 até o número de inteiros na lista;list->int'''
    i=0
    if lista[0]!=1:
        return 1
    while i<len(lista)-1:
        if abs((lista[i])-(lista[i+1]))!=1:
            return lista[i+1]-1
        i=i+1
    else:
        return lista[-1]+1