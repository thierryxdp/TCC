def maiores(lista,n):
    list.sort(lista)
    for numero in lista:
        if numero>n:
            return lista[numero:]