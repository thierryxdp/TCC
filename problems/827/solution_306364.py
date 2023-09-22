def qtd_divisores(n:int) ->int:
    """Essa função, dado um número inteiro,
    calcula e retorna quantos divisores ele possui"""
    
    divisores = []
    
    for i in list(range(1,n+1)):
        if n % i == 0:
            divisores.append(i)
    return len(divisores)