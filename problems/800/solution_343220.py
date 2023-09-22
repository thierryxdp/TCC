"""
"""
def total(lista_compras, mercado):
    prod_disponiveis = list(mercado.keys())
    preco = list(mercado.values())
    soma = 0
    i = 0
    for produto in lista_compras:
    	if produto == prod_disponiveis[i]:
        	i += 1
        	soma = soma + preco[i]
            
    return round(soma, 2)