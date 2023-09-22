def filtraMultiplos(lista,num):
    """usei o metodo de for para fazer com que minha função
encontrasse os multiplos de num na lista e colocassem em outra lista baseada na original"""
    multiplos = list()
    for x in lista:
        if x % num == 0:
            multiplos.append(x)
    return multiplos