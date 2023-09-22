def qtd_divisores(num):
    """Funcao que, dado um numero, retorna quantos divisores ele possui.
    float -> float"""
    divisores = list(filter(lambda x:num%x==0, list(range(1,num+1))))
    return len(divisores)