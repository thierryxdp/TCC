lista_de_compras = ['biscoito', 'chocolate', 'farinha']

produtos = {
    'amaciante': 4.99,
    'arroz': 10.90,
    'biscoito': 1.69,
    'cafe': 6.98,
    'chocolate': 3.79,
    'farinha': 2.99
    }

def total(lista_de_compras, produtos):
    custo = 0
    
    for x in lista_de_compras:
        if x in produtos:
            custo += produtos[x]
            
    return custo