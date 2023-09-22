def soma_h(n):
    """função que calcula e retorna o valor de H;int-->float"""
    a=1
    for i in range(1,n+1):
        a+=1/i
    return soma