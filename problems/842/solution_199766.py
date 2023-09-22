x=0
y=0
def pontos_por_time(l1,l2):
    if l1[2][0]>l1[2][1]:
        x=(x+3) and y=(y+0)
    elif l1[2][0]==l1[2][1]:
        x=(x+1) and y=(y+1)
    else:
        x=(x+0) and y=(y+0)
    if l2[2][0]>l2[2][1]:
        x=(x+0) and y=(y+3)
    elif l1[2][0]==l1[2][1]:
        x=(x+1) and y=(y+1)
    else:
        x=(x+3) and y=(y+0)
        return [l2[0]]+[y]+[l2[1]]+[x]