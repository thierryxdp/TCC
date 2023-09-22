#Start your python function here
def filtra_pares(x):
    l=x[0]%2
    m=x[1]%2
    n=x[2]%2
    o=x[3]%2
    if l==0 and m==0 and n==0 and o==0:
        return (x[:],)
    elif l!=0 and m==0 and n==0 and o==0:
        return (x[1:],)
    elif l==0 and m!=0 and n==0 and o==0:
        return (x[0],x[3:])
    elif l==0 and m==0 and n!=0 and o==0:
        return (x[:2],x[3])
    elif l==0 and m==0 and n==0 and o!=0:
        return (x[:3],)
    elif l!=0 and m!=0 and n==0 and o==0:
        return (x[2:],)
    elif l!=0 and m==0 and n!=0 and o==0:
        return (x[1],x[3])
    elif l!=0 and m==0 and n==0 and o!=0:
        return (x[1:3],)
    elif l==0 and m!=0 and n!=0 and o==0:
        return (x[0],x[3])
    elif l==0 and m!=0 and n==0 and o!=0:
        return (x[0],x[2])
    elif l==0 and m==0 and n!=0 and o!=0:
        return (x[0:2],)