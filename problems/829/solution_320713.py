def soma_h (numero):
    """Recebe um número inteiro n e o soma seguindo
    a sequência 1 + 1/2 + 1/4 +...+1/n. 
    int -> float"""
    divisao = 1
    for indice in range(2, numero+1):
        divisao += 1/indice
    return round(divisao, 2)