def filtraMultiplos(lista_numeros,n):
    '''Dada uma lista com numeros retorna uma nova lista com os multiplos de n
    list,int -> list'''
    lista = []
    c = 0
    while c < len(lista_numeros):
        if lista_numeros[c] % n:
            lista.append(lista_numeros[c])
    c += 1
   	return lista