def filtraMultiplos(lista, numero):
    contador = 0
    nova_lista = []
    while contador <= len(lista):
        if lista[contador]%numero == 0:
            nova_lista = nova_lista + lista[contador]
    return nova_lista