#Start your python function here
def pontos_por_time(l):
    pa1=0
    pa2=0
    pb1=0
    pb2=0
    a1=l[0][2][0]
    b1=l[0][2][1]
    a2=l[1][2][1]
    b2=l[1][2][0]
    if a1>b1:
        pa1 = 3
    elif a1==b1:
        pa1=1
        pb1=1
    else:
        pb1 = 3
    if a2>b2:
        pa2 = 3
    elif a2==b2:
        pa2=1
        pb2=1
    else:
        pb2 = 3
    
    pontosa = pa1+pa2
    pontosb = pb1+pb2
    x= {l[0][0]:pontosa, l[0][1]:pontosb}
    return x