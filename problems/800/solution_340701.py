def total(lista_de_compras,precos):
    ''' recebe uma lista de compras e os preços dos produtos que disponiveis em uma loja e
    retorna a soma dos preços dos produtos disponiveis na loja que estão na lista de compras'''
	valor_total= []
    for i in lista_de_compras:
        if i in precos:
            list.append(valor_total,i)
    return sum(valor_total)