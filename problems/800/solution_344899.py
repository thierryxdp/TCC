def total(listaCompras, precoProdutos):
    """ função que  recebe uma lista de compras e um dicinário com com os preços
    	de cada produto disponível em uma loja. retorna o valor total dos intens
        da lista disponiveis na loja. list, dict --> float """
    contaTotal = 0
    for intem in listaCompras:
        contaTotal += precoProdutos [item]
    return round(contaTotal, 2)