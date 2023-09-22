def filtraMultiplos(lista,n):
    """Esta função filtra os múltiplos de um número n, recebendo como entrada
    uma lista de números e o número, retornando uma outra lista
    contendo todos os elementos da lista original que forem divisíveis por n."""
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            lista1 = lista1 + (lista[i],)
        i = i + 1
    return list(lista1)