def maiores(lista,n):
    if n not in lista:
        lista.append(n)
        lista.sort()
        a = lista.index(n)
        lista_numeros = lista[a+1:]
        rep = lista_numeros.count(n)
        return lista_numeros[rep:]