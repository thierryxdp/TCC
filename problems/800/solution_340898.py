def total (lista_compras, valores):
    '''dada uma lista de compras e um dicionario contendo o 
       preço de cada produto disponivel em uma loja, retorna o
       valor total dos itens da lista que estejam disponiveis
       nesta loja.
       : list, dict -> float
    '''
    valor_total = 0
    for produto in lista_compras:
        if produto in valores:
            valor_total = valor_total + valores[produto]
    return valor_total