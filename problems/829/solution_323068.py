def soma_h(num):
    """Função que faz o somatório das frações
    até o denominador N atribuido
    int -> float"""
    f = 0
    for n in range(1, num + 1):
        f = f + 1/n
    return round(f,2)