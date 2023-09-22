"""
"""
def total(lista_compras, mercado):
    prod_disponiveis = list(mercado.keys())
    soma = 0
    i = 0
    for produto in lista_compras:
        while i < len(lista_compras):
            if produto == prod_disponiveis[i]:
        		i += 1
        		soma = soma + mercado.get(produto)
    return soma