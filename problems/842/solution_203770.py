def pontos_por_time(l):
    pontos={}
    

    a=bool(l[0][2][0]>l[0][2][1])
    b=bool(l[0][2][0]=[0][2][1])
    c=bool(l[1][2][0]<[1][2][1])
    d=bool(l[1][2][0]=[1][2][1])
     
    if l[0][0]='Cormengo': 
        cor=(a+c)*3+(b+c)
        if cor=6:
            fla=0
        if cor=4:
            fla=1
        if cor=3:
            fla=3
        if cor=1:
            fla=4
        else:
            fla=6
    else:
        fla=(a+c)*3+(b+c)
        if fla=6:
            cor=0
        if fla=4:
            cor=1
        if fla=3:
            cor=3
        if fla=1:
            cor=4
        else:
            cor=6
     pontos('Cormengo')=str(cor)
     pontos('Flaminthians')=str(fla)
     return pontos