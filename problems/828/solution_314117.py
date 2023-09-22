def primos(n):
    """ """
    primo=[]
    for i in range(1,n+1):
        if n%i==0:
            primo=primo +[i]
    if len(primo)> 2:
        return False
    else: return True