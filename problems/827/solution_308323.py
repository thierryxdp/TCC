def qtd_divisores(numero):
    """Função que conta quantos divisores um número tem.
    int->int"""
    q=0
    for i in range(1,numero+1): 
        if numero % i == 0:
            q+=1
    return q