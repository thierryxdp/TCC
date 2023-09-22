def filtraMultiplos(lista, n):
    """dada uma lista calcula e retorna os multiplos de n
list,int -> list"""
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            multiplos= multiplos+[lista[i]]
        elif lista[i]%n != 0:
            None
        i = i + 1
    return multiplos