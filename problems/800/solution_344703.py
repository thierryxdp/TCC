def total(lista,dict={}):
    despesa = 0.0
    
    for i in lista:
        despesa = despesa + dict[i]
        
    return round(despesa,2)