def qtd_divisores(n):
    i=1
    for i in range (1,n):
        if n % i ==0:
            i=i+1
            print len(i)