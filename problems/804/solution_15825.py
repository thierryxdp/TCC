def filtra_pares(tup):
    lista1 =(tup)
    lista2 =()
    for valor in lista1:
        if valor%2==0:
            lista2.append(valor)
            return lista2