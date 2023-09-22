def qtd_divisores(x):
    '''retorna quantos divisores um numero x de entrada tem
    int -> int'''
    qtd = 0
    if x <=0:
        return 0
    for i in range(1,x):
        if x % i == 0:
            qtd = qtd + 1
            return qtd