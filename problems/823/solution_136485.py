def faltante(lista):
    #formato [1,n]
    contador =0
    faltante = 0
    
    while contador<len(lista):
        if lista[contador] - lista[contador-1]!=1:
            faltante = lista[contador]
            contador+=1
        else:
            contador+=1
    return faltante