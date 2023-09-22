def filtraMultiplos(lista,n):
    '''Filtra os numeros de uma lista divisiveis por n.
    list,int -> list'''
    final = []
    contador = 0
    while contador < len(lista):
        if (lista[contador])%n==0:
            final.append(lista[contador])
        contador += 1
    return final