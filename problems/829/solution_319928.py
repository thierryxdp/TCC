def soma_h(n):
    """Funcao que retorna o valor H
    int->inst"""
    soma=1
    for num in range(2, n+1):
        soma=soma+(1/num)
    return round(soma,2)