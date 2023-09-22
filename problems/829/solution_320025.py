def soma_h(n):
    """Essa funcao calcula e retornaa soma
       H = 1 + 1/2 + 1/3 + ... + 1/n
       int, -> float"""
    
    soma = 1
    for i in range(2,n+1):
        soma += round((1/i),2)
    return soma