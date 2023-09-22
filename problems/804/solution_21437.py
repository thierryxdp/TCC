filtra_pares(a,b,c,d):
    lista = [a,b,c,d]
    lista_valida = []
    for elem in lista:
    if elem > 0:
        lista_valida.append(elem)
        return lista_valida