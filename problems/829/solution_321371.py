def soma_h(n):
    """calcula e retorna o valor de h com n termos;
    int, float->"""
    
    soma = 1
    i= 1
    while i == n:
        resultado = soma/i
        i = i + 1
    return round(resultado, 2)