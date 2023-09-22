def total(lista_de_compras, dicionario_precos):
    '''Função que dada uma lista de compras e um dicionario 
    contendo o preço de cada produto disponível, retorna
    o valor total dos itens da lista que estejam disponiveis.
    lista_de_compras -> list
    return -> float'''
    
    i = 0
    lista = lista_de_compras
    dicionario = dicionario_precos
    somatorio = 0
    for i in range(len(lista)):
        if lista[i] in dicionario:
            somatorio += dicionario[lista[i]]
    return round(somatorio, 2)