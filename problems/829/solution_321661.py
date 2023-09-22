def soma_h(n):
    """função que calcula e retorna o valor de H;int-->float"""
    soma=0
    for i in range(1+ n+1):
        soma= soma+1/i
    return soma