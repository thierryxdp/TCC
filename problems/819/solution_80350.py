def filtraMultiplos(lista,n):
    '''filtra e retorna os numeros divisíveis pela entrada n. lista->list/n-->/return-->list'''
    multiplos=()
    elemento=0
    while elemento<len(lista):
        if lista[elemento]%n==0:
            multiplos = multiplos+(lista[elemento],)
        elemento= elemento +1
    return multiplos