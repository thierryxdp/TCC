def  filtraMultiplos(lista,n):

    lista_mult = []
    i=0
    while i<len(lista):
        if lista[i]%n == 0:
           list.append(lista_mult, lista[i])       
        i=i+1       
    return lista_mult