def total(lista=[], dic={}):
    cont = 0.0
    
    for i in lista:
        cont+=dic[i]
    return round(cont,2)