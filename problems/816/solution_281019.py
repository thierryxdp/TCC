def maiores(lista_numero,n):
    cont = 0
    lista2_numero = []
    while cont < len(lista_numero):
        if lista_numero[cont] > n:
            lista2_numero.append(lista_numero[cont])
        cont = cont + 1
    return lista2_numero