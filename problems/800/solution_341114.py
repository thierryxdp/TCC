def total(lista, preco):
    """recebe uma lista de compras e um dicionario contendo os itens de um 
    supermercado e seus respectivos precos e retorna o valor total dessa compra
    list, dictionary -> float"""
    
    soma = 0
    for i in range(len(lista)):
        produto = lista[i]
        
        if produto in list(dict.keys(preco)):
            soma += dict.get(preco, produto)
        
    return round(soma, 2)