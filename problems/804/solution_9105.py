par(n):
    return n%2==0
impar(n):
    return n%2==1
filtra_pares(a):
    if par(int(a[0]))==True:
        x1=a[0]
    elif impar(int(a[0]))==True:
        x1=''
    elif par(int(a[1]))==True:
        x2=a[1]
    elif impar(int(a[1]))==True:
        x2=''
    elif par(int(a[2]))==True:
        x3=a[2]
    elif impar(int(a[2]))==True:
        x3=''
    elif par(int(a[3]))==True:
        x4=a[3]
    elif impar(int(a[3]))==True:
        x4=''
    return (x1+x2+x3+x4)