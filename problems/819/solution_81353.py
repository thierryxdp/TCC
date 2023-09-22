def filtraMultiplos(lista,numero):
    contador = 0
    nova_lista = []
    while contador <= len(lista):
        if lista[contador]%2==0:
            nova_lista = lista[contador]
        else:
            nova_lista = nova_lista
        contador = contador + 1
    return lista