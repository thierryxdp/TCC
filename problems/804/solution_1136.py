def oito(a,b,c,d):
    lista1 = [a,b,c,d]
    lista2 = filter(lambda x: x % 2 == 0,lista1) 
    return list(lista2)