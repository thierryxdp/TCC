#Start your python function here
def pt1j1(r1):
    gt1j1=(r1[0])
    gt2j1=(r1[1])
    if (gt1j1)>(gt2j1):
        return 3
    else:
        return 0
def pt1j2(r2):
    gt1j2=(r2[0:0])
    gt2j2=(r2[1:1])
    if (gt1j2)<(gt2j2):
        return 3
    else:
        return 0
def pft1(r1,r2):
    return ((pt1j1(r1))+(pt1j2(r2)))

def pt2j1(r1):
    gt2j1=(r1[1])
    gt1j1=(r1[0])
    if (gt2j1)>(gt1j1):
        return 3
    else:
        return 0
    
def pt2j2(r2):
    gt2j2=(r2[1:1])
    gt1j2=(r2[0:0])
    if (gt2j2)<(gt1j2):
        return 3
    else:
        return 0
    
def pft2(r1,r2):
    return ((pt2j1(r1))+(pt2j2(r2)))
    



def pontos_por_time(x):
    x=(x[0])
    y=(x[1:1])
    t1=(x[0])
    t2=(y[0:0])
    r1=(x[2])
    r2=(y[2:2])
    gt1j1=(r1[0])
    gt1j2=(r2[0:0])
    gt2j1=(r1[1])
    gt2j2=(r2[1:1])
    

    
    
    
    
    
    

    return {(t1):str (pft1(r1,r2)),(t2):str (pft2(r1,r2))}