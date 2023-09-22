def maiores(listacompleta, n):
    '''função que mostraapenas os numeros de uma lista que são maiores que n. list -> list'''
        if [n]>(listacompleta):
            return []
        if [n]<(listacompleta):
            list.sort(listacompleta)
            return listacompleta