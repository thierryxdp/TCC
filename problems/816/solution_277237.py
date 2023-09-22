def maiores(lista, n):
    nova_lista = list()
    for numero in lista:
        if numero > n:
        	nova_lista.append(numero)
    nova_lista.sort()
    return nova_lista