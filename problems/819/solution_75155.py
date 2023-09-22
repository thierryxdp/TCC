def filtraMultiplos(lista,numero):
    multiplos=[]
    x=0
    while lista[x]>=len(lista):
        if lista[x]%numero==0:
            multiplos=multiplos+[lista[x]]
        x=x+1
    return multiplos