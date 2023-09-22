def maiores(lista_numeros, n):
    for i in lista_numeros:
        if i < n:
            lista_numeros.remove(i)
            
    return lista_numeros