def qtd_divisores(x):
    c=1
    while c<= x:
        a= x%c
        c=c+1
        if a==0:
            return(c-1)