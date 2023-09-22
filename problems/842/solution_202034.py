#Start your python function here
def pontost1(gt1,gt2):
    if gt1>gt2:
        return 3
    if gt1<gt2:
        return 0
    else:
        return 1
    
def pontost2(gt2,gt1):
    if gt2>gt1:
        return 3
    if gt2<gt1:
        return 0
    else:
        return 1
    

def pontos_por_time(j1):
    j1=[[str(t1),str(t2),r1]]
    j2=[[str(t2),str(t1),r2]]
    return {str(t1):pontost1, str(t2):pontost2}