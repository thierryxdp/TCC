def soma_h(n:float):
    """Função que calcula o valor de H dado o número
       termos N."""
    soma = 0
    for i in range(1,n+1):
        H = 1/i
        soma += H
    return round(soma,2)