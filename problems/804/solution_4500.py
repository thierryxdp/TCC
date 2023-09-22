def filtra_pares([a,b,c,d]):
    "Função que filtra os números pares de uma tupla com 4 elementos"
    lista1 = [a,b,c,d]
    lista2 = []
    for valor in lista1:
        if valor % 2 == 0:
            lista2.append(valor)
            return lista2