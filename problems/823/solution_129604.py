def faltante(lista):
    x=0
    count=0
    while x<=len(lista)-1:
        if not lista[x]==lista[x+1]:
            count=count+1
        x=x+1
    return lista[x+1]