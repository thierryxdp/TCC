def filtraMultiplos(lista,n):
    """Função que, dada uma lista e um numero n, retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n
       list,int -> list"""
    multiplos=[]
    for x in lista:
        if x % n == 0:
            multiplos.append(x)
        return multiplos