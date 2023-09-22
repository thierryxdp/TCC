def total(lista=[],dict={}):
    cont=0.0
    i=1
    while i in lista:
        cont+=dict[i]
        i+=1
    return round(cont,2)