def qtd_divisores(n):
    nn=[1,2,3,5,6,7,8,9,13,17,19,23,29,37,41,43,47,53,59,61,67,71,73,79,83,89,n]
    r=0
    if n<0:
        return 0
    for i in nn:
        if n%i==0:
            r+=1
    return r