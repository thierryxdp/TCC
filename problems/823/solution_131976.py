def faltante(listaL):
    a=list(range(1,listaL[-1]+1))
    cont=0
    while cont<len(a):
        cont=cont+1
        if listaL[cont-1]!=a[cont-1]:
            return a[cont-1]
        elif listaL==a:
            return a[-1]+1