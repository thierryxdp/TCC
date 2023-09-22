def maiores(lista_numero,n):
    ADD = list.append(lista_numero, n)
    organiza = list.sort(lista_numero)
    local = list.index(lista_numero, n)
    return lista_numero[local:]