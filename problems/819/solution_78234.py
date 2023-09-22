def filtraMutiplos(lista , n):
    lista_valida = []
    for elem in lista:
        if elem % n ==0:
            lista_valida.append(elem)
    return lista_valida