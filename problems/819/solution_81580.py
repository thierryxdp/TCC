def filtraMultiplos(lista,num):
    i=0
    lista_multiplos=[]
    while i<len(lista):
        if lista[i]%num!=0:
            lista_multiplos+=lista[i]
        i+=1
    return lista_multiplos