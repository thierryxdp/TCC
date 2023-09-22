def soma_h(n):
    """ retorna o valor de h dado o numero de entrada n"""
    """ int -> int """
    soma=1
    for num in range(2, n+1):
        soma = soma + (1/num)
    return round(soma, 2)