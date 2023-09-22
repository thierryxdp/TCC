def maiores(lista_numero, n): 
    lista_maiores = []
    for i in lista_numero:
        if i > n:
            lista_maiores.append(i)
    return lista_maiores