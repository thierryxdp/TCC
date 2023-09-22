def pontos_por_time(lista): 
    [[[Cormengo,Flaminthias,[a,b]],[Cormengo, Flaminthias,[c,d]]] = lista
    dici = {Cormengo:0, Flaminthias:0}
     if a>b and c>d:
        return dici[Cormengo] +=6
     elif a>b and c=d:
        return dici[Cormengo] +=4
     elif a=b and c>d:
        return dici[Cormengo] +=4
     elif a<b and c<d:
        return dici[Flaminthias] +=6
     elif a<b and c=d:
        return dici[Flaminthias] +=4
     elif a=b and c<d:
        return dici[Flaminthias] +=4
     else:
        return dici[Flaminthias,Cormengo] += 2