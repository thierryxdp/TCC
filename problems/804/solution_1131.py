#Start your python function here
def filtra_pares(n):
    n=tuple(n)
    n2=[]   
    
    if (n[0] % 2 == 0):
        n2.append(n[0])
    if (n[1] % 2 == 0):
        n2.append(n[1])
    if (n[2] % 2 == 0):
 		n2.append(n[2])
    if (n[3] % 2 == 0):
        n2.append(n[3])     
    return tuple(n2)