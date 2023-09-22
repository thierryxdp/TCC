def primo(n):
    """Este código recebe um número e retorna True se for primo, e 
    False, se não for.
    Recebe: int
    Retorna: Bool"""
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