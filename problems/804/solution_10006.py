#Start your python function here
        
def filtra_pares(t):
    "essa função retonrna valores pares de uma tupla"
    x=0
    if t[0]%2==0:
    	a=t[0]
    else :
    	a=()
    if t[1]%2==0:
    	b= a[0]+t[1]
    else :
    	b=a[0]
    if t[2]%2==0:
    	c=a[0]+b[0]+t[2]
    else :
    	c=a[0]+b[0]
    if t[3]%2==0:
    	d=a[0]+b[0]+c[0]+t[3]
    else :
    	d=a[0]+b[0]+c[0]   
    t1=(d)
    return t1