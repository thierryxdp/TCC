def filtraMultiplos(lista,n):
    '''Funcao que, dada uma lista de numeros e um numero n, retorna uma nova lista com os numeros da lista originais que sao divisiveis por n; list (com inteiros) -> list (com inteiros)'''
    multiplos=[]
    proximo=0
    while lista[proximo]%n=0:
        if lista[proximo]%n==0:
            multiplos=multiplos+[lista[proximo]]
        proximo=proximo+1
    return multiplos