def conta_numero(numero,matriz):
    cont={}
    num=1
    lista=str.split(matriz)
    for p in lista:
        if p in cont:
            cont[p]=dict.get(cont,p)+1
        else:
            cont[p]=1
    return cont