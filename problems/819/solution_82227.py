def filtraMultiplos(lista, numero):
    resutado=[]
    x=0
    while x <= len (lista)-1:
        if lista[x] % numero == 0:
            y = lista[x]
            resultado = []
            list.append(resultado,y)
            x = x + 1
        elif x <= len (lista):
            lista[x]% numero != 0           
    return resultado