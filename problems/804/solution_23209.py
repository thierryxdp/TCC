#Start your python function here
def filtra_pares(t):
    r=()
    if(t[0]%2==0):
        r=r+t[0]
    elif(t[0]%2==1):
    	r=r+0
    if(t[1]%2==0):
        r=r+t[1]
    elif(t[1]%2==1):
    	r=r+0
    if(t[2]%2==0):
        r=r+t[2]
    elif(t[2]%2==1):
    	r=r+0
    if(t[3]%2==0):
        r=r+t[3]
    elif(t[3]%2==1):
    	r=r+0
    return r