def total(lista,tabela):
	'''recebendo a lista de compras e a tabela de preços do supermercado(em dicionário)
	informa o valor da compra
	lista,dicio->float'''
    valor=0
    for produto in lista:
        if produto in tabela:
            valor+=produto
    return valor
    
# Escolha nomes elucidativos para suas variáveis