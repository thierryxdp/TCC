def divisores(num):
    b=[]
    if num>0:
        b.append(num)
    for i in range(1, num//2+1):
        if num % i == 0: 
            b.append(i)
    return b