def pontos_por_time(l):
    x=0
    y=0
    if l[0][2][0]>l[0][2][1]:
        x=(x+3) 
        y=(y+0)
    elif l[0][2][0]==l[0][2][1]:
        x=1 
        y=1
    else:
        x=(x+0)
        y=(y+0)
    if l[1][2][0]>l[1][2][1]:
        x=(x+0) 
        y=(y+3)
    elif l[1][2][0]==l[1][2][1]:
        x=(x+1) 
        y=(y+1)
    else:
        x=(x+3) 
        y=(y+0)
        return {chaves:l[1][0]]+[y]+[l[1][1]]+[x]}