#Start your python function here
def pontos_por_time(lis):
    sp1=0
    sp2=0
    if lis[0][2][0]>lis[0][2][1]:
        sp1=+3
    elif lis[0][2][1]>lis[0][2][0]:
        sp2=+3
    elif lis[0][2][1]==lis[0][2][0]:
        sp1=+1
        sp2=+1
    elif lis[1][2][0]>lis[1][2][1]:
    	sp2=+3
    elif lis[1][2][1]>lis[1][2][0]:
        sp1=+3
    else lis[1][2][0]==lis[1][2][1]:
        sp1=+1
        sp2=+1
    return [sp1]