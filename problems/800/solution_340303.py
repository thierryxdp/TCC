def total(listinha,precos):
    '''recebe uma lista de compras e um dicionário 
contendo o preço de cada produto disponível em
uma determinada loja, e retorna o valor total dos
itens da lista que estejam disponíveis nesta loja.'''
    valor=0
    for prod in listinha:
        if prod in precos:
            valor+=precos[prod]
    return round(valor,2)