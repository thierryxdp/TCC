def maiores(lista,n):
    lista.sort()
    if n in lista:
        ola = lista.index(n)
        nov = lista[ola:]
        return nov
    else:
        lista.append(n)
        lista.sort()
        ola= lista.index(n)
        nov = lista[ola:]
        nov.remove(n)
        return nov
    def acima_da_media(lista,n>=6):
        resp = maiores(lista,n)
        return resp