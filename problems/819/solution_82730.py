def filtraMultiplos(lista,n):
    i=0
    resto=0
    nova_lista=[]
    while i < len(lista):
        if lista[i] % n in resto:
            nova_lista=+ lista[i]
        i= i+1
        return nova_lista