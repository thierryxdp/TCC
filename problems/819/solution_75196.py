def filtraMultiplos(lista, n):
    """retorna uma lista contendo os elementos da lista original que forem divisiveis por n"""
    lista2 = []
    a=0
    while a<=len(lista)-1:
        if lista[a]%n==0:
            lista2.append(lista[a])
        a=a+1
    return lista2