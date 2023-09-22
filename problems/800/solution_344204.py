def total(ls, d):
    """Recebe uma lista de compras e um dicionário com os preços de cada produto disponível
    na loja, retornando o valor total dos itens na lista.
    assinatura: tuple(list, dict) --> float
    testes:
    total() ==
    total() ==
    """
    sol=[]
    for i in ls:
        if i in d:
            sol.append(d[i])
    return round(sum(sol),2)