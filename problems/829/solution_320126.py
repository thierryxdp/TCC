def soma_h(n):
    """funcao que calcula e retorna a soma de H,
       onde H= 1 + 1/2 + 1/3+ 1/4 + ... + 1/n

       int-> float
    """
    soma=0

    for i in range(1,n+1):
         soma = soma + 1/i

    return round(soma,2)