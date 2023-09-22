def filtraMultiplos(lista,n):
    '''Dado uma lista de numeros números inteiros, será retornada uma lista
    de números divisiveis por n. (lista, int => lista)'''

    lista2 = []
    i = 0
    
    while i < len(lista):
        
        if n * (lista[i] // n) == lista[i]:
            
            lista2.append(lista[i])
            
            i = i + 1
            
        else:
            i = i + 1

    return lista2