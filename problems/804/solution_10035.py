#Start your python function here
        
def filtra_pares(t):
    "essa função retonrna valores pares de uma tupla"
    x=0
    if t[0]%2==0:
    	a=t[0]
    else :
    	a=('')
    if t[1]%2==0:
    	b=t[1]
    else :
    	b=()
    if t[2]%2==0:
    	c=t[2]
    else :
    	c=()
    if t[3]%2==0:
    	d=t[3]
    else :
    	d=()    
    t1=(a,b,c,d)
    return t1