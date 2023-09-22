#Start your python function here
#Start your python function here
def pt1j1(r1):
    if (r1[0])>(r1[1]):
        return 3
    else:
        return 0
def pt1j2(r2):
    if (r2[0])>(r2[1]):
        return 3
    else:
        return 0
def pft1(r1,r2):
    return int(pt1j1(r1)+pt1j2(r2))

def pt2j1(r1):
    if (r1[0])<(r1[1]):
        return 3
    else:
        return 0
    
def pt2j2(r2):
    if (r2[0])<(r2[1]):
        return 3
    else:
        return 0
    
def pft2(r1,r2):
    return int(pt2j1(r1)+pt2j2(r2))
    



def pontos_por_time(x):
    x=(x[0])
    y=(x[1])
    t1=(x[0])
    t2=(y[0:])
    r1=(x[2])
    r2=(y[2])
    r2=(y[2])
    

    
    
    
    
    
    

    return {(t1):print(pft1),(t2):[pft2]}