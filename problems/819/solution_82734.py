def filtraMultiplos(lista,n):
    i=0
    mtp= lista[i]%n
    nova_lista=[]
    while i < len(lista):
        if mtp=0:
            nova_lista=+ lista[i]
        i= i+1
        return nova_lista