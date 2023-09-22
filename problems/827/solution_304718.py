def qtd_divisores(num):
    n = np.arange(1,num)
    d = num % n
    zeros = d == 0
    print (n[zeros])