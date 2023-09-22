def filtra_pares ([a, b, c, d]):
    lista1=[a, b, c, d]
    lista2=[]
    
    for n in lista1:
        if n%2==0:
            lista2.append(n)
    return lista2