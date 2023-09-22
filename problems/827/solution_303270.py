def qtd_divisores(n):
    """Esta função recebe um número e retorna a quantidade de 
    divisores que ele possui"""
    divisores = []
    posicao = 1
    
    
    while posicao <= n:
        if n%posicao ==0:
            list.append(divisores, posicao)
        posicao = posicao + 1
    return len(divisores)