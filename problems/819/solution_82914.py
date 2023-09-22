def filtrarMultiplos(lista, n):
    
    i = 0
    nova_lista = []
    while i < len(lista):
        if lista[i] % n == 0:
            nova_lista.append(lista[i])
	return nova_lista;