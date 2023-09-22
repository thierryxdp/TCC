def qtd_divisores(x):
    """Conta quantos divisores um número tem.
    assinatura: int--> int
    """
    resultado= [i for i in range(1,x+1) if x % i == 0]
    return len(resultado)