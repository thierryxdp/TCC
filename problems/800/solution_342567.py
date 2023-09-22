def total(ls_compras, produtos = {}):
    produtos = {
    'amaciante':4.99,
    'arroz':10.90,
    'biscoito':1.69,
    'cafe':6.98,
    'chocolate':3.79,
    'farinha':2.99
  }
    for e in ls_compras:
        if e in produtos:
            soma = sum(produtos.values())
            return soma