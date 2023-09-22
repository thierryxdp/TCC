def maiores(listamaiores, n):
    '''função que mostraapenas os numeros de uma lista que são maiores que n. list -> list'''
    if [n]>(listamaiores):
        return []
    if [n]<(listamaiores):
        list.sort(listamaiores)
        return listamaiores