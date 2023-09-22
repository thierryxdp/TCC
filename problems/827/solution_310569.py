def qtd_divisores(n):
    aux=0
    if n<=0:
        return 0
    else:
        for x in range(1,n//2+1):
            if n%x==0:
                aux+=1
             return aux+1