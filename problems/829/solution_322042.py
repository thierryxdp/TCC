def soma_h(num):
    """Calcula a soma de H, dado um numero qualquer: int --> float"""
    soma = 0
    for eita in range(num +1):
        if eita >0:
            soma = soma + (1/eita)
    return round(soma,2)