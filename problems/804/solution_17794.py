#Start your python function here
def filtra_pares(a,b,c,d):
    ''' função que define se os elementos de uma tupla são pares
    	int, int, int,int ---> float'''
    if a//2==0 and b//2==0 and c//2==0 and d//2==0:
        return (a,b,c,d)
    elif a//2==0 and b//2==0 and c//2==0 and d//2!=0:
        return(a,b,c)
    elif a//2==0 and b//2==0 and c//2!=0 and d//2!=0:
        return(a,b)
    elif a//2==0 and b//2!=0 and c//2!=0 and d//2!=0:
        return (a,)
    else:
        return 'inválido'