def melhor_volta(x):
    m=min((x[0]+x[1]+x[2]+x[3]+x[4]+x[5]))
    contcor=0
    contcur=0
    for e in x:
        contcor=contcor+1
        for i in e:
            contcur=contcur+1
            if i==m:
                return (contcor,contcur,m)