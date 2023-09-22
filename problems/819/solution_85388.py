def filtraMultiplos(lista_numeros,n):
    '''Recebe uma lista de numeros e um numero e retorna outra lista com os elementos que forem divisiveis por n; list,int->list'''
    multiplos=0
    i=0
    while i<len(lista_numeros):
        if (lista_numeros[i]%n)==0:
            list.append(multiplos, lista_numeros[i])
            i=i+1
            return multiplos