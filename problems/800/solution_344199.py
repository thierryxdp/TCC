def total(compr, precos):
    """Recebe uma lista de compras e um dicionário com os preços de cada produto disponível
    na loja, retornando o valor total dos itens na lista.
    assinatura: lista, dic --> int
    """
    sol=[]
    for i in compr:
        if i in precos:
            sol.append(i[precos])
    return sol