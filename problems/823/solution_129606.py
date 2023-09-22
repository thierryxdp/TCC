def faltante(lista):
    x=1
    lista2=[]
    while x<=len(lista)-1:
        if lista[x]==lista[x-1]:
            lista2.append(lista[x+1])
        x=x+1
    return lista2