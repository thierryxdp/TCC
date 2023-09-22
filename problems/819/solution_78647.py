def filtraMultiplos(lista:list, n:int) -> list:
    """Essa função, dada uma lista e um número inteiro n
    como parâmetros de entrada, retorna uma nova lista com todos
    os números da lista original divisiveis por n"""
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i]%n == 0:
            divisiveis.append(lista[i])
        i += 1
    return divisiveis