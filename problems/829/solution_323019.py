def soma_h(numero):
    """Função que calcula e retorna o valor H de uma expressão somatória com N termos. Entrada -> Int; Saída float"""
    H = 1/numero
    soma = 0
    for termos in range(1, numero +1):
        soma = soma + (1/termos)
    
    return round(soma, 2)