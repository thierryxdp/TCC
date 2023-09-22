def filtraMultiplos(lista,n):
    """Funcao que retorna todos os multiplos de n"""
    indice = 0
    multiplos = []
    while indice < len(lista):
        y = list.pop(lista,indice)
        if y % == 0:
            multiplos = multiplos + [y]
    return multiplos