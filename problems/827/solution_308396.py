def qtd_divisores(num):
    """"""
    divisores=0
    for n in range(num+1):
        if n!=0:
            if num%n==0:
                divisores+=1
    return divisores