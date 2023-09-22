def qtd_divisores(N):
    if N<=0:
        return 0
    n = 1
    num=[]
    while(n<N):
        if(N%n==0):
            num.append(n)
        else:
            pass
        n += 1
    num.append(N)
    return len(num)