def soma_h(n):
    """
"""
    soma = 0
    contador = 0
    num = 1
    while contador!=n:
        soma+= (1/num)
        num+= 1
        contador+=1
    return round(soma,2)