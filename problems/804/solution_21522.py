def filtra_pares(t,c,d,a):
    lista1= (t,c,d,a)
    lista = []   
    for valor in lista1 :
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)