def faltante(lista):
    i=1
    n=0
    a=0
    lista2=list(range(lista[0],lista[len(lista)-1],1))
    if lista==lista2:
        return lista[len(lista)-1]+1