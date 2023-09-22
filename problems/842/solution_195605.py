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
    
    

def pontos_por_time(list_um,list_dois):
    """xxxxxxxxxxxx"""
   
   
    gols_um = [n1,n2]
    gols_dois = [n3,n4]
    
    list_um = [x1, x2, gols_um]
    list_dois = [x2, x1, gols_dois]
    
    if caso_1(n1,n2,n3,n4):
        return {str(x1):6, str(x2):0}
    if caso_2(n1,n2,n3,n4):
        return {str(x1):4, str(x2):1}
    if caso_3(n1,n2,n3,n4):
        return {str(x1):3, str(x2):3}
    if caso_4(n1,n2,n3,n4):
        return {str(x1):2, str(x2):2}
    if caso_5(n1,n2,n3,n4):
        return {str(x1):0, str(x2):6}
    if caso_6(n1,n2,n3,n4) :
        return {str(x1):1, str(x2):4}#Start your python function here