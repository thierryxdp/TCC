def qtd_divisores(n):
    divisores=0
    for i in range(n):
        if i!=0 and n%(i)==0:
            divisores+=1
    return divisores