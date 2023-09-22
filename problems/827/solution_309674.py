def qtd_divisores(num):
    '''
       Dado um número a função retorna quantos divisores esse
       número possui.
       int -> int
    '''
    total=0
    for i in range(1, num//2+1):
        if num%i == 0:
            total= total + i
    return total