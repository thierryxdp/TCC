def pontos_por_time(l):
    pontos={}
    

    a=bool(l[0][2][0]>l[0][2][1])
    b=bool(l[0][2][0]==l[0][2][1])
    c=bool(l[1][2][0]<l[1][2][1])
    d=bool(l[1][2][0]==l[1][2][1])
     
    
    cor=((a+c)*3)+(b+d)
    if cor==6:
        fla=0
    if cor==4:
        fla=1
    if cor==3:
        fla=3
    if cor==1:
        fla=4
    if cor==2:
        fla=2
    if cor==0:
        fla=6
    else:
        fla=0
        
        
    
    pontos[l[0][0]]=cor
    pontos[l[0][1]]=fla
    return pontos