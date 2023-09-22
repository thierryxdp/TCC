def total (lista, dicio):
    valor=0
    a=dict.values(dicio)
    round(valor,2)
    for chave in dicio:
        if dicio[chave]==lista:
            valor+=sum(a(chave)) 
            
    return  valor