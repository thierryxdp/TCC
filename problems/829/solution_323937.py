def soma_h(n):
    """Função que dada um número inteiro n, calcula e retorna o valor h com
    n termos (como dado na função);
    int -> float"""
    h = 0
    for num in range(1, n+1):
        h = h + 1/num
    return round(h,2)