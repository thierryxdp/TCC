total(lista, dic):
    """Recebe uma lista de compras e um dicionário com o preço dos 
    produtos e retorna o valor total da compra feita com a lista, de 
    acordo com os produtos disponíveis na loja.
    assinatura: list, dict --> float
    testes:
    total(['bolacha', 'banana', 'beringela'], {'bolacha':4.50, 'morango':8, 'banana':10.50, 'beringela':3}) == 18.0
    total(['uva', 'maça'], {'uva':8, 'maça':1}) == 9
    """
    total = 0
    for prod in lista: 
        total = total + dic[prod]
    return round(total, 2)