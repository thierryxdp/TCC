def filtraMultiplos(lista,n):
    x=0
    while x < len(lista):
        if lista[x]%n!=0:
             lista.pop(x)
        else:
            x=x+1
            return lista