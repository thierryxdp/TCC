total(compr, precos):
    """Recebe uma lista de compras e um dicionário com 
os preços de cada produto disponível na loja, retornando
o valor total dos itens na lista.
Assinatura: list, dict -> int
"""
    log=[]
    for i in compr:
        if i in precos:
            log.append(precos[i])
    return round(sum(log),2)