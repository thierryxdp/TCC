def soma_h(n):
    """Dado um número, retorna o resultado da equação H. int>float"""
    resultado=0
    for i in range(1,n+1):
        resultado += 1/i
    return round(resultado,2)