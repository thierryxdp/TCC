def total(compras,precos):
    '''Funcao que recebe de entrada uma lista de compras e 
    um dicionario referente aos precos dos produtos de uma 
    loja. O retorno eh a soma dos valores dos produtos
    da lista de compras disponiveis para venda na loja.
    list, dict -> float'''
    valor_total = 0
    for produto in compras:
        if produto in precos:
            valor_total += precos[produto]
    return round(valor_total,2)

#TESTE
# lista_de_compras = ['feijao', 'arroz', 'acucar', 
# 'chocolate', 'banana']
# lista_de_precos = {'feijao': 2.75, 'macarrao': 3.89, 
# 'acucar': 4.50, 'fil de frango': 15.79, 'chocolate': 3.99,
# 'arroz': 18.88}
# total(lista_de_compras, lista_de_precos) == 30.12