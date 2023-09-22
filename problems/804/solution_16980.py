#Start your python function here
def filtra_pares (a,b,c,d):
    t=a,b,c,d
    t2=[]
    if t[0]%2==0:
        t2.append(a)
        if t[1]%2==0:
            t2.append(b)
        if t[2]%2==0:
            t2.append(c)
        if t[3]%2==0:
            t2.append(d)
        return t2
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        return t2