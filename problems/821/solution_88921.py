def fatorial(x):
    num=list(range(x+1))
    list.remove(num,0)
    i=0
    fatorial=1
    while i<len(num):
        fatorial=fatorial*num[i]
        i=i+1
    return fatorial