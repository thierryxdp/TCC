def filtraMultiplos(lista,n):
    '''Dado uma lista de numeros números inteiros, será retornada uma lista
    de números divisiveis por n. (lista, int => lista)'''

    lista2 = []
    i = 0
    d = lista[i] // n
    
    while i < len(lista):
        
        if n * d == lista[i]:
            lista2.append(lista[i])
        i = i + 1
            
        else:
            i = i + 1

    return lista2