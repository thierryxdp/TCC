def total(lista=[],dict={}):
    '''funçao que recebe uma lista de compras e dicionário com os preços das mercadorias da loja e retorna o valor dos itens da lista'''
    cont = 0.0
    for i in lista:
        cont+=dict[i]
    return round(cont,2)