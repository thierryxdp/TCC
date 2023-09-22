def faltante(lista):
    j=0
    lista2=range(1,len(lista+1))
    while j <len(lista):
        if not lista2[j] in lista:
            j=j+1
    return lista2[j]