def total(lista_de_compras, produtos):
    '''Recebe uma lista de compras e um dicionário que associa produtos a
    valores e retorna o preço somado dos produtos que estavam na lista
    (list,dict -> int).'''
    separados = lista_de_compras.split()
    soma = 0
    for produto in separados:
        if produto in produtos.keys():
            soma = soma + produtos[produto] 
    round(soma, 2)
    return soma