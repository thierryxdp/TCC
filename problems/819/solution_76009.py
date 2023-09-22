#list(int),int->list
def filtraMultiplos(lista,n):
    lista1= []
    for n in lista:
        if n%2 == 0: 
            lista1.append(n)
        if n%3 == 0: 
            lista1.append(n)
        if n%4 == 0: 
            lista1.append(n)
        if n%5 == 0: 
            lista1.append(n)
        if n%6 == 0: 
            lista1.append(n)
        if n%7 == 0: 
            lista1.append(n)
        if n%8 == 0: 
            lista1.append(n)
        if n%9 == 0: 
            lista1.append(n)
    lista1.sort()
    return lista1