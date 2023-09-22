def fatorial(n):
    """Função que calcula o fatorial do número n inserido"""
    p=n
    while p>1:
        n=n*(p-1)
        p=p-1
    return n