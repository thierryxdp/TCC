def filtra_pares(lista):
    lista2=[]
    for c in lista:
        if c%2==0:
            lista2.append(c)
            lista2=tuple(lista2[:])
            return lista2
        lista3=[]
        for c in lista:
            if c%2==0:
                lista3.append(c)
                lista3=tuple(lista2[:])
                return lista3