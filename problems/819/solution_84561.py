def filtraMultiplos(lista,n):
    lista_final = []
    result = 0
    while result < len(lista):
        if lista[result]%n == 0:
            lista_final = lista_final + [lista[result],]
        result = result + 1
    return lista_final