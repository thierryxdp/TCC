def total (lista, dicio):
   
    valor=0
    a=dict.values(dicio)
    
    for chave in dicio:
        if dicio[chave]==lista:
            valor+= a
    return round(a,2)