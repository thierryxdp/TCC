def filtraMultiplos (lista, n):
    '''Dada uma lista de numeros e um numero n, retorna
    uma lista dos numeros multiplos de n;
    list,float-> list'''
    indice= 0
    n_elementos= len(lista)
    multiplos=[]
    while indice < n_elementos - 1:
        if lista[indice] % n == 0:
            list.append(multiplos,lista[indice])
        indice += 1

    return multiplos