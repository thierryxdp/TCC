def fatorial(n):
    """Recebe um numero e calcula o farotial desse numero.
    Assinatura:int --> int"""
    x = 1
    for i in range(1,n+1):
        x = x*i
    return x