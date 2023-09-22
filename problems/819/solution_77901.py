def filtraMultiplos(lista,n):
    """Funcao que filtra os multiplos de um numero n; list,int -> list"""
    i = 0
    multiplos = []
    while i<len(lista):
        if lista[i]%n == 0:
            list.append(multiplos,lista[i]) 
        i = i + 1
    return multiplos