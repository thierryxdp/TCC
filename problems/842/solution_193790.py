def pontos_por_time(lista):
    
    lista1=lista[0]
    placar1=lista1[2]
    
    if placar1[0]>placar1[1]:
        k=3
        x=0
    if placar1[0]<placar1[1]:
        k=0
        x=3
    if placar1[0]==placar1[1]:
        k=1
        x=1
        
    lista2=lista[1]
    placar2=lista2[2]
    
    if placar2[0]>placar2[1]:
        t=3
        y=0
    if placar2[0]<placar2[1]:
        t=0
        y=3
    if placar2[0]==placar2[1]:
        t=1
        y=1

    c=k+y
    f=x+t

    n=lista1[0]
    m=lista1[1]
    
    d={n:c,m:f}

    if n=="Vasínthians" or n=="Fluminantos" or n=="Santasco" or n=="Botagama" or n=="Flumipaulo" or n=="Paulo da Gama":
    	d={m:f,n:c}

    return d