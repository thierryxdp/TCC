def filtrarMultiplos(lista, n):
    '''Dados uma lista e um número n retorna uma lista com os multiplos de n
    list, int -> list'''
    i = 0
    nova_lista = []
    while i < len(lista):
        if lista[i] % n == 0:
            nova_lista.append(lista[i])
        i+=1
	return nova_lista;