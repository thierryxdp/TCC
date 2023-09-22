def soma_h(n):
    """ Função que receben com entrada e retorna o valor de H
         int ---> int"""
    c = []
    for h in round(1,n+1):
    c.append(1/h)
    return round((sum(c)),2)