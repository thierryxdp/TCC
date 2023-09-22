def pontos_por_time(l):
    pontos={}
    

    a=bool(l[0][2][0]>l[0][2][1])
    b=bool(l[0][2][0]==l[0][2][1])
    c=bool(l[1][2][0]<l[1][2][1])
    d=bool(l[1][2][0]==l[1][2][1])
     
    
    cor=(a+c)*3+(b+c)
    if cor==6:
        fla=0
    if cor==4:
        fla=1
    if cor==3:
        fla=3
    if cor==1:
        fla=4
    else:
        fla=6
    
    pontos[l[0][0]]=str(cor)
    pontos[l[0][1]]=str(fla)
    return pontos