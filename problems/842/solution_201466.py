def pontos_por_time(lista):
    lista1=lista[0]
    lista2=lista[1]
    placar1=lista1[2]
    placar2=lista2[2]
    if placar1[0]>placar1[1]:
        j1t1=3 
        j1t2=0
    elif placar1[1]>placar1[0]:
        j1t2=3
        j1t1=0   
    elif placar1[0]==placar1[1]:
             j1t1=j1t2=1
    elif placar2[0]>placar2[1]:
             j2t2=3 
             j2t1=0
    elif placar2[1]>placar2[0]:                 
             j2t1=3
             j2t2=0
    else:
             j2t2=j2t1=1          
    return x=j1t1+j2t1
           y=j1t2+j2t2
           {lista1[0]:x,lista1[1]:y}