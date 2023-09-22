def filtraMultiplos(lista,n):
    """Função que, dada uma lista e um numero n, retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n
       list,float -> list"""
    contador = 0
    multiplos = []
    while contador < len(lista):
        if lista[contador]%n == 0:
            multiplos += [lista[contador]]
        contador += 1
    return multiplos