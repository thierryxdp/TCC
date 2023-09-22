def filtraMultiplos(lista, num):
    """Funcao que, dado uma lista de numeros e um numero, retorna outra lista contendo todos elementos da lista original que forem divisiveis pelo numero.
    list, float -> list"""
    multiplos = list(filter(lambda x: x%num==0, lista))
    return multiplos