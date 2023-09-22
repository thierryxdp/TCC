def auxiliar(lista, num):
    """Funcao que, dado uma lista de numeros e um numero, retorna outra lista contendo todos elementos da lista original que forem divisiveis pelo numero.
    list, float -> list"""
    i = 0
    while i < len(lista):
        if lista[i]%num == 0:
            return True
        i = i+1
def filtraMultiplos(lista, num):
    """Funcao que, dado uma lista de numeros e um numero, retorna outra lista contendo todos elementos da lista original que forem divisiveis pelo numero.
    list, float -> list"""
    multiplos = list(filter(auxiliar(lista, num), lista))
    return multiplos