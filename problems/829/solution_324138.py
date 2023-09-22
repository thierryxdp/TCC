def soma_h(n):
    """ Retorna a soma da série H em n termos.
Assinatura: int --> int
Teste:
soma_h(1) == 1.0
soma_h(2) == 1.5
"""
    H= 1/n
    ls= []
    for i in range(1, n+1):
        ls.append(1/i)
    return round(sum(ls), 2)