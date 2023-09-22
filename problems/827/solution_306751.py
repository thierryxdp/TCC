def qtd_divisores(n):
    '''Fazer uma funcao que calcule quantos divisores n tem e retorne a quantidade;
    int -> int'''
    
    divisor = []
    
    for i in range(1, n + 1):
        if n%i == 0:
            list.append(divisor,i)
    return (divisor)