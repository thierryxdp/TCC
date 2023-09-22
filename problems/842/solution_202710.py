def pontos_por_time(lista1):
    x=0
    y=0
    l1=[]
    l2=[]
    l1.append(lista1[0][0])
    l2.append(lista1[0][1])
    if lista1[0][1][0]>lista1[0][1][1]:
       x=x+3
       y=y+0
    elif lista1[0][1][0]==lista1[0][1][1]:
       x=x+1
       y=y+1
    elif lista1[0][1][0]<lista1[0][1][1]:
       x=x+0
       y=y+3
    if lista1[1][1][1]>lista1[1][1][0]:
       x=x+3
       y=y+0
    elif lista1[1][1][1]==lista1[1][1][0]:
       x=x+1
       y=y+1
    elif lista1[1][1][1]<lista1[1][1][0]:
       x=x+0
       y=y+3    
    l1.append(x)
    l2.append(y)
    l1.append(l2)
    
    return lista1[1][2][0]