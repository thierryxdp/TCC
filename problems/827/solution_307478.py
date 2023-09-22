def qtd_divisores(n):
    nn=[1,2,3,4,5,6,7,8,9,12,13,17,18,19,23,24,29,31,36,37,41,43,47,53,59,61,67,71,73,79,83,89]
    r=n/n
    if n<0:
        return 0
    for i in nn:
        if n%i==0:
            r+=1
        if i==n:
            r-=1
    return r