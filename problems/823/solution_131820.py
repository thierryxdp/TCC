def faltante (lista):
    
    list.sort (lista)
    contador = 2
    
    while 1 in lista and len(lista)<lista[-1]:
        if contador not in lista:
            return contador
        contador = contador + 1

    if 1 not in lista:
        return 1
    if 1 in lista and len(lista) == lista[-1]:
        return lista[-1] + 1