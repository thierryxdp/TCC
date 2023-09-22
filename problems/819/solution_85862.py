def filtraMultiplos(lista,n):
    """Executar uma lista com todos multiplos de n da lista original;
    list, int -> list"""
    x = 0
    lista_nova = []
    while x < len(lista):
        if lista[x] % n == 0:
            lista_nova += [lista[x],]
        x += 1
    return lista_nova