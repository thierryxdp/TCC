#Start your python function here
def filtra_pares(t):

    x=0
    n=0
   	c=(n,)
    for n in t:
        
        if n%2 == 0:
            
            c[x]=(n,)
            x+=1
    return c