def total(lista,produtos):
    'retorna a soma dos valores de uma lista de compras dos produtos disponiveis na loja'
    'lista,dict---float'
    valor=0
    estoque=list(produtos.keys())
    for produto in lista:
        if produto in estoque:
            valor+=produtos[produto]
    return round(valor,3)