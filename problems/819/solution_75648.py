def filtraMultiplos(lista,numero):
    resultado=[]
    i=0
    while i<len(lista):
        if lista[i]%numero==0:
            list.extend(resultado,lista[i])
    i+=1 
    return resultado