#Start your python function here
def filtra_pares(n):
    n=tuple(n)
    n2=tuple()
    int (index)=1
    
    if (n[1] % 2 == 0):
        n2[index] = n[1]
        index = index+1
    if (n[2] % 2 == 0):
        n2[index] = n[2]
        index = index+1
    if (n[3] % 2 == 0):
        n2[index] = n[3]
        index = index+1
    if (n[4] % 2 == 0):
        n2[index] = n[4]
        index = index+1        
    return n2