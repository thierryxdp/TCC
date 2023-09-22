def filtraMultiplos(lista,n):
    i=0
    nova_lista=list()
    while i<len(lista):
        mtp=lista[i]%n
        if mtp==0:
            nova_lista=+lista[i]
            list.append(nova_lista,lista[i])
        i=i+1
    return [nova_lista]