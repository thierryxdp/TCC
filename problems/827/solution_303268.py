def qtd_divisores(n):
    """..."""
    divisores = []
    posicao = []
    
    
    while posicao <= n:
        if n%posicao ==0:
            list.append(divisores, posicao)
        posicao = posicao + 1
    return len(divisores)