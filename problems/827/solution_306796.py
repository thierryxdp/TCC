def qtd_divisores (n):
    '''
    	essa função recebe um número e conta quantos divisores o mesmo tem
        int -> int
    '''
    x = []
    for i in range(1, n+1):
        if n%i == 0:
            x.append(i)
    return x