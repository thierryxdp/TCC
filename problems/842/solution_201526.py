#Start your python function here
def pontos_por_time(CF):
    f1= CF[0]
    f2= CF[1]

    Pf1= f1[2]
    Pf2= f2[2]

    if    Pf1[0]>Pf1[1]:
        Pc1=3
        Pf1=0
    elif    Pf1[0]<Pf1[1]:
        Pc1=0
        Pf1=3
    else:
        Pc1=1
        Pf1=1
    if    Pf2[0]>Pf2[1]:
        Pc2=3
        Pf2=0
    elif    Pf2[0]<Pf2[1]:
        Pc2=0
        Pf2=3
    else:
        Pc2=1
        Pf2=1
    PC=Pc1+Pc2
    PF=Pf1+Pf2

    return {f1[0]:PC,f1[1]:PF}