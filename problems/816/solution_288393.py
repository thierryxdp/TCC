def maiores(lista, n):
    
    if n in lista:

        lista.sort()
        t = lista.index(n)
        resultado = lista[t+1:]

        return resultado