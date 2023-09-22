def qtd_divisores (n):
    '''
    	essa função recebe um número e retorna a quantidade de divisores que a mesma tem
        int->int
    '''
    x = 1
    while x <= n:
        y = n % x
        x = x+1
        if x == 0:
            return x