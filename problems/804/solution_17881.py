#Start your python function here
def filtra_pares(a):
    ''' função que define se os elementos de uma tupla são pares
    	int, int, int,int ---> float'''
    if a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2==0:
        return a
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2!=0:
        return (a[0], a[1], a[2],)
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[0], a[1],)
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[0],)
    else:
        return ()