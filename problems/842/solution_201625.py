def pontos_por_time(lista1, lista2):
    a=lista1[2][0]
    b=lista1[2][1]
    c=lista2[2][0]
    d=lista2[2][1]
    time1= lista1[0]
    time2= lista1[1]
    lista1= [time1, time2, [a, b]]
    lista2= [time1, time2,[c, d]]
    if (a==b) and (c==d):
        {time1: 2,
                time2: 2}
    elif (a>b) and (c>d):
      	{time1: 6,
                time2: 0}
    elif (a<b) and (c<d):
        {time1: 0,
                time2: 6}
    elif (a>b) and (c==d):
       	{time1: 4,
                time2: 1}
    elif (a<b) and (c==d):
      	{time1: 1,
                time2: 4}
    elif (a==b) and (c>d):
        {time1: 4,
                time2: 1}
    elif (a==b) and (c<d):
     	{time1: 1,
                time2: 4}
    elif (a>b) and (c<d):
     	{time1: 3,
                time2: 3}
    elif (a<b) and (c>d):
        {time1: 3,
                time2: 3}