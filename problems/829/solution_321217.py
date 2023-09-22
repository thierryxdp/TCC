def soma_h(N):
    """função que calcula e retorna o valor de H, através dos N termos fornecidos pelo
    valor de entrada N;
    Entrada: int
    Saída: float"""
    x = range(1,N+1)
    resultado = 0
    
    for numero in x:
        H = 1 / numero
        resultado = resultado + H
    return round(resultado,2)