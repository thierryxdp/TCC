def filtraMultiplos(lista, n):
    """A função recebe como entrada uma lista de ints e 
    um int n e retorna uma outra lista contendo apenas os
    múltiplos de n da lista original."""
    lista_multiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            lista_multiplos.append(lista[i])
        i += 1
    return lista_multiplos