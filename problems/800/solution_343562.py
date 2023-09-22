def total(lista,dict_precos):
    '''Retorna o valor a ser pago pelos produtos que estejam na lista de compra e que estejam disponiveis na loja
       lista,dict->int'''
    preco_total = 0
    for produto in lista:
        if produto not in  dict_precos:
            dict_precos[produto] = 0
        preco_item = dict_precos[produto]
        preco_total += preco_item
    return round(preco_total,2)
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis