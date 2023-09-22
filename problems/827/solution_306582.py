def qtd_divisores(numero):
    """Funcao que conta quantos divisores o numero de entrada tem;
    int -> int"""
    divisores=[]
    for possivel_divisor in range(1,numero+1):
        if numero%possivel_divisor==0:
            divisores+=[possivel_divisor]
    return len(divisores)