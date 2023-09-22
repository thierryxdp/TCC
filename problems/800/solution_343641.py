def total(lista, precos):
    """Dada uma lista de compras e um dicionário contendo
os valores de determinados produtos de uma loja, retorna
o valor total dos itens da lista que estão disponíveis na loja.
assinatura: list, dict --> float
casos de teste:
total(['biscoito', 'chocolate'], {'biscoito':1.69, 'chocolate':3.79}) == 5.48
total(['biscoito', 'chocolate', 'batata'], {'biscoito':1.69, 'chocolate':3.79, 'batata': 1.99}) == 7.47
total(['biscoito', 'chocolate'], {'biscoito':1.69, 'chocolate':3.79, 'batata': 1.99}) == 5.48
"""
    val = 0
    for item in lista:
        val= val + dict.get(precos, item)
    return round(val, 2)