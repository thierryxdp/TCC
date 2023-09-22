def filtraMultiplos(lista,numero):
    multiplos=[]
    x=0
    while (lista[x])>=numero or lista[x]==numero:
        if lista[x]%numero==0:
            multiplos=multiplos+[lista[x]]
        x=x+1
    return multiplos