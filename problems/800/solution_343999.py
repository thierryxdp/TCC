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
    valor_final = 0
    
    for item in lista_de_compras:
        if item in produtos:
            valor_final += produtos[item]
            
    return valor_final