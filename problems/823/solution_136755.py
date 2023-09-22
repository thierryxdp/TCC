def faltante(lista):
    j=0
    lista2=range(1,n)
    while j <len(lista):
        if not lista[j] in lista:
            j=j+1
    return lista2[j]