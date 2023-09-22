def maiores(lista, n):
    if n in lista:

        lista.sort()
        t = lista.index(n)
        resultado = lista[t+1:]

        return resultado

    if n not in lista:
    
        lista.append(n)
        lista.sort()
        t = lista.index(n)
        resultado = lista[t+1:]

        return resultado