def fatorial(n):
    """Calcula o fatorial de um número n"""
    i=0
    f=n-i
    fat=[]
    while (i< n-1):
        if int(f)>=1:
            fat=fat+[f]
            i=i+1
    a= 1         
    while (i<len(fat)):
        a=a*int(fat[i])
    return a