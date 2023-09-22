def filtraMultiplos(lista, n):
    """Recebe uma lista de números, e um número,
       e retorna uma lista com os números que são divisiveis.
    	lst, int -> lst"""
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos.append(lista[i])
        i+=1
    return multiplos