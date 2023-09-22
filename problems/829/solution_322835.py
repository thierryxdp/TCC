def soma_h(n):
    """Dado um número inteiro N, a função calcula e retona
    o valor de H, sendo H=1+(1/2)+(1/3)+...+(1/n).
    Parametros de Entrada: int
    Retorna: float"""

    soma=0
    
    for i in list(range(1,n+1)):
        soma= soma+(1/i)

    return round(soma,2)