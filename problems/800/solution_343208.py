"""
"""
def total(lista_compras, mercado):
    prod_disponiveis = list(vendendo.keys())
    soma = 0
    i = 0
    for produto in lista_compras:
        if produto == prod_disponiveis[i]:
        	i += 1
        	soma = mercado.get(produto)
    return soma