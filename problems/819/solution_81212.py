def filtraMultiplos(lista,n):
    """Funcao que retorna todos os multiplos de n"""
    indice = 0
    multiplos = []
    while indice <= len(lista) - 1:
       y = list.pop(lista,indice)
       indice += 1
        multiplos = multiplos + y
    return multiplos