def soma_h(n):
    """Esta é a função que dado um número n retorna o valor de H= 1+1/2+1/3+1/4+...+1/N, int -> float"""
    soma = 0
    for x in range(1, n + 1):
        
        inverso = (1/x)
        soma = soma + inverso

    return round(soma,2)