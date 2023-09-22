def fatorial(n):
    lista = [n]
    while n != 1:
        n = n - 1
        lista += [n,]
    
    lista2 = str.split(lista,',')
    return lista2