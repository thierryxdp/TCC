def filtraMultiplos(lista,n):
    """Função que, dada uma lista e um numero n, retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n
       list,int -> list"""
    multiplos=()
    proximo=0
    while proximo < len(lista):
        if lista[proximo]%2 == 0:
            multiplos += [lista[proximo],]
        proximo += 1
    return multiplos