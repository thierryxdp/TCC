def caso_1(n1,n2,n3,n4):
    if n1>n2 and n4>n3:
        return True
        
def caso_2(n1,n2,n3,n4):
    if (n1>n2 and n4==n3) or (n1==n2 and n4>n3):
        return True
        
def caso_3(n1,n2,n3,n4):
    if (n1>n2 and n4<n3) or (n1<n2 and n4>n3):
        return True
        
def caso_4(n1,n2,n3,n4):
    if n1==n2 and n4==n3:
        return True
         
    
def caso_5(n1,n2,n3,n4):
    if n1<n2 and n4<n3:
        return True
        
        
        
def caso_6(n1,n2,n3,n4):
    if (n1<n2 and n4==n3) or (n1==n2 and n4<n3):
        return True
    
    

def pontos_por_time(x1,x2,n1,n2,n3,n4):
    """xxxxxxxxxxxx"""
   

    if caso_1(n1,n2,n3,n4):
        return {x1:6, x2:0}
    elif caso_2(n1,n2,n3,n4):
        return {x1:4, x2:1}
    elif caso_3(n1,n2,n3,n4):
        return {x1:3, x2:3}
    elif caso_4(n1,n2,n3,n4):
        return {x1:2, x2:2}
    elif caso_5(n1,n2,n3,n4):
        return {x1:0, x2:6}
    if caso_6(n1,n2,n3,n4):
        return {x1:1, x2:4}