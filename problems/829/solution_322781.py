def soma_h(n):
    """Retorna o valor da soma H;
int -> float"""
    soma = 0

    for divisor in range(1,n+1):
        soma += 1/divisor
        
    return round(soma, 2)