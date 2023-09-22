def filtraMultiplos (lista, numero):
    """Função que recebe uma lista de numeros e um numero e retorna outra lista contendo todos os numeros da lista original divisiveis por n;
        list, int -> list."""
    multiplos = []
    proximo = 0
    while proximo < len (lista):
        if lista [proximo]% numero == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo= proximo + 1
    return multiplos