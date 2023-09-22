def total(lista=[], dict={}):
    '''função que recebe uma lista de compras e um dicionário que informa o valor dos produtos disponíveis na loja e retorna o valor total a ser pago pelos itens da lista de compras que estão disponíveis na loja, com duas casas decimais.
    lista, dicionário -> float'''
    
    cont = 0.0
    for i in lista:
        cont = cont + dict[i]
    return round(cont, 2)