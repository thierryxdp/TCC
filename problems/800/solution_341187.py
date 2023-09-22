def total(c, d):
    """A função recebe uma lista de compras e um dicionário contendo o preço de cada item em um comércio como parâmetro e retorna o gasto total do cliente com as compras.
       list, dict -> int"""
    l = []
    for i in range(len(c)):
        if c[i] in list(dict.keys(d)):
            l = l + [d[c[i]]]
    return round(sum(l),2)
#Testes:
#lista = ['farinha', 'chocolate', 'biscoito']
#preços = {'amaciante': 4.99, 'arroz': 10.90, 'biscoito': 1.69, 'cafe': 6.98, 'chocolate': 3.79, 'farinha': 2.99}
#total(lista, preços)--> 8.47

#lista = ['macarrão', 'queijo', 'guaraná']
#preços = {'queijo': 5.99, 'papel higiênico': 12.87, 'batata inglesa': 14.30}
#total(lista, preços)--> 5.99