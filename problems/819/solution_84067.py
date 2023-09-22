def filtraMultiplos(lista,n):
    '''função que filtra os múltiplos do
    número n
    lista -> lista'''
    multiplos = []
    for item in lista:
        if item%n==0:
            multiplos.append(item)
    return multiplos