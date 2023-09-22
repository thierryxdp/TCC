def filtraMultiplos(lista_numeros,n):
    lista_final = []
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i]%n==0:
            lista_final += [lista_numeros[i]]
        i+=1
    return lista_final