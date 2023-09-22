#list(int),int->list
def filtraMultiplos(lista,n):
    lista1= []
    for c in lista:
        if c%n == 0: 
            lista1.append(c)
            return lista1