def filtraMultiplos(lista, n):
     """Funçao que filtra os multiplos de um numero n, 
        recebe uma lista e retorna outra lista contendo todos os 
        elementos da lista original que forem divisiveis por n."""
        lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            lista1 = lista1 + (lista[i],)
        i = i + 1
    return list(lista1)