def soma_h(n):
    """Função que calcula a expreção de h, esta sendo
    a soma de suceciva de 1 + 1/(todos o números de 1 a n)
    int -> float"""
    h = 0
    for i in range(1,n+1):
        h += 1/i
    return round(h, 2)