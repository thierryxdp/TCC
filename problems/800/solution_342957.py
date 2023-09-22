def total (lista, dicio):
   
    valor=0
    a=list(dict.keys(dicio))
    b=list(dict.values(dicio))
    c=[]
    for chave in lista:
        if dicio[chave] in b:
            valor+= dicio[chave]
    return  valor