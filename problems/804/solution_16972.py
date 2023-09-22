#Essa função retorna com os valores pares de uma tupla com
# quatro elementos
# int,int,int,int ->int
def filtra_pares (a,b,c,d):
    t=a,b,c,d
    t2=[]
    if a%2==0:
        t2.append(a)
        if b%2==0:
            t2.append(b)
        if c%2==0:
            t2.append(c)
        if d%2==0:
            t2.append(d)
        return t2
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
        return t2