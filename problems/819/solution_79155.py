def filtraMultiplos(lista,numero):
    i=0
    listaFinal=[]
    while i<len(lista):
        if lista[i]%numero==0:
            listaFinal=listaFinal+lista[i]
        i=i+1
    return listaFinal