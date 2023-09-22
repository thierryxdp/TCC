def soma_h(n):
    """Retorna a soma da séria H em n termos.
Teste: soma_h(1) == 1
soma_h(2) == 1.5
assinatura: int --> int
"""
    serie = 1/n
    ret = []
    for passo in range(1, n+1):
        ret.append(1/passo)
    return sum(ret)