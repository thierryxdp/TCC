def filtraMultiplos (lista,n):
    '''kg'''
    multiplos=[]
    n_lista=0
    lista_primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89,97]
    while n_lista<len(lista):
        if lista[n_lista] in lista_primos:
            multiplos= multiplos+ lista[n_lista]
            n_lista= n_lista+1
        else:
            multiplos=multiplos
            n_lista= n_lista+1
    return multiplos