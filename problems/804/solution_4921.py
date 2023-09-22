#Start your python function here
def filtra_pares(t):

    x=0
   	
    for n in t:
        
        if n%2 == 0:
            
            t[x]=(n,)
            x+=1
    return t