def filtraMultiplos(lista,n):
    """Funcao que retorna todos os multiplos de n"""
    indice = 0
    multiplos = []
    while indice <= len(lista) - 1:
        y = list.pop(lista,indice)
        if y % n == 0:
            multiplos = multiplos + [y]
            indice += 1
    return multiplos