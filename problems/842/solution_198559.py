def pontos_por_time(lista):
    
    [[Cormengo,Flaminthias,[a,b]],[Cormengo, Flaminthias,[c,d]] = lista
   
    if  a>b and c>d:
     return str'Cormengo' + str'->' + 6
    elif a>b and c=d:
     return str'Cormengo' + str'->' + 4 + str'Flaminthias' + str'->' + 1
    elif a=b and c>d:
     return str'Cormengo' + str'->' + 4 + str'Flaminthias' + str'->' + 1
    elif a<b and c<d:
     return str'Flaminthias' + str'->' + 6
    elif a<b and c=d:
     return str'Cormengo' + str'->' + 1 + str'Flaminthias' + str'->' + 4
    elif a=b and c<d:
     return str'Cormengo' + str'->' + 1 + str'Flaminthias' + str'->' + 4