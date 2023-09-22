def filtraMultiplos (lista,n):
    '''Dado uma lista de numeros e um numero, retorna uma nova lista com todos os multiplos 
    presentes na lista
    list, int -> list'''
    lista1 = [] 
    i=0
    while i<len(lista) :
        if lista[i] % n == 0 : 
            lista1 = lista1 + [lista[i]]
        i = i + 1
    return lista1