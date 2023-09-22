def maiores(lista_numero,n):
    if n in lista_numero:
        return lista_numero[n:]
    if n not in lista_numero:
        list.append(lista_numero,n)
        list.sort(lista_numero)
        return lista_numero[n:]