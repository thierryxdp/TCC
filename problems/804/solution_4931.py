#Start your python function here
def filtra_pares(t):

    x=0
   	c=()
    for n in t:
        if n%2 == 0:
            c+=n,
            x+=1
    return c