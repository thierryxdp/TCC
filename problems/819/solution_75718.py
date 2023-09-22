def filtraMultiplos(lista,n):
    """Função que, dada uma lista e um numero n, retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n
       list,int -> list"""
    multiplos=()
    proximo=0
    for multiplos in lista:
        if lista[proximo]%n == 0:
            list.append(lista[proximo])
        proximo += 1
    return multiplos