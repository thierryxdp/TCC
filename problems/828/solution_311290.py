def primo(n):
    """..."""
    divisores = []
    posicao = 1
    
    while posicao <= n:
        if n%posicao == 0:
            list.append(divisores, posicao)
        posicao = posicao + 1
    
    if len(divisores) == 2:
        return True
    else:
        return False