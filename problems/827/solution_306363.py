def qtd_divisores(n:int) ->int:
    """comentário"""
    divisores = []
    for i in list(range(1,n+1)):
        if n % i == 0:
            divisores.append(i)
    return len(divisores)