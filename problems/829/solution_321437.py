def soma_h(numero):
    """ Função que receben com entrada e retorna o valor de H
         int ---> int"""
    c = []
    for h in round(1,numero+1):
        c.append(1/h)
    return round((sum(c)),2)