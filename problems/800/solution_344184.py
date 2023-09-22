def total(listaDeCompras, precosDosProdutos):
    """
    	Recebe uma lista com nomes de produtos e um dicionário
        contendo o nome do produto e seu preço.
        Retorna o valor somado dos preços dos produtos contidos na lista.
        list, dict --> float
    """
    contaTotal = 0
    for item in listaDeCompras:
        contaTotal += precosDosProdutos[item]
    return round(contaTotal, 2)