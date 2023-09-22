def faltantes(lista):
    falt=[]
    prox=0
    for a in range (lista[0],(lista[-1]+1)):
        if a != lista[prox]:
            falt=falt+[lista[prox]]
            a=a+1
            prox=prox+1
    return falt