def pontos_por_time(informacao):
    x=0
	y=0
    if l1[2][0]>l1[2][1]:
        x=(x+3) 
        y=(y+0)
    elif l1[2][0]==l1[2][1]:
        x=1 
        y=1
    else:
        x=(x+0)
        y=(y+0)
    if l2[2][0]>l2[2][1]:
        x=(x+0) 
        y=(y+3)
    elif l1[2][0]==l1[2][1]:
        x=(x+1) 
        y=(y+1)
    else:
        x=(x+3) 
        y=(y+0)
        return [l2[0]]+[y]+[l2[1]]+[x]