def maiores(lista,n):
    lista_final = []
    for i in lista:
        if i > n:
            lista_final.append(i)
            return lista_final