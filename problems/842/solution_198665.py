def pontos_por_time(lista): 
   [[[Cormengo,Flaminthias,[a,b]],[Cormengo, Flaminthias,[c,d]]] = lista
    dici = {Cormengo:0, Flaminthias:0}
     if a>b:
           dici[Cormengo] += 3
     elif c>d:
           dici[Cormengo] +=3
     if b>a:
           dici[Flaminthias] +=3
     elif d>c:
           dici[Flaminthias] += 3
     else:
           dici[Cormengo] +=2
           dici[Flaminthias] += 2