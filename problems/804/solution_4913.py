#Start your python function here
def filtra_pares(t):

    
    for n in t:
        if n%2 == 0:
    		t=t+(n,)
    return t