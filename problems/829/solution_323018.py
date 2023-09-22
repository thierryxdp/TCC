def soma_h(numero):
    """A função calcula o resultado da sequência de somas até a fração
    1/N, onde N é é um número inteiro dado por entrada.
    int -> float"""
    
    H = 1/numero
    soma = 0
    for termos in range(1, numero +1):
        soma = soma + (1/termos)
    
    return round(soma, 2)