filtra_Multiplos(lista_numeros,n):
    lista_final = []
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i]%n==0:
            lista_final += [lista_numeros[i]]
    return lista_final