#Start your python function here
def r1(gt1,gt2):
    if gt1>gt2:
        return 3
    if gt1<gt2:
        return 0
    else:
        return 1
    
def r2(gt2,gt1):
    if gt2>gt1:
        return 3
    if gt2<gt1:
        return 0
    else:
        return 1
    

def pontos_por_time(x):
    t1=(x[0])
    t2=(x[1])
    x=[t1,t2,r1],[t2,t1,r2]
    rf=r1+r2
    
    j1=[[str(t1),str(t2),r1]]
    j2=[[str(t2),str(t1),r2]]
    return {str(t1):rf, str(t2):rf}