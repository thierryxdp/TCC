def filtraMultiplos(lista, num)
	n=0
    nova_lista = []
    while n < len(lista):
        if lista[n] % num == 0:
            nova_lista.append(lista[n])
            
            n +=1
    return nova_lista