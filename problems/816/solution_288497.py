def maiores(lista, n):
    def maiores(lista, n):
    if n in lista:
        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]
        return listafinal
    if n not in lista:
        lista.append(n)
        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]
        return listafinal