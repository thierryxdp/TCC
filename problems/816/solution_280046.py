def maiores(lista_numeros, n):
    for i in lista_numeros:
        if i > n:
            lista_numeros.remove(i)
    lista_numeros.sort()
    return lista_numeros

print(maiores([6, 13, 14, 16, 7], 17))