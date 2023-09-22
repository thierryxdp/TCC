def qtd_divisores(num):
    n = n.arange(1,num)
    d = num % n
    zeros = d == 0
    print (n[zeros])