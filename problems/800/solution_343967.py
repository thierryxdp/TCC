"""recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja"""
def total(lista_de_compras, produtos):
    valor_final = 0
    
    for item in lista_de_compras:
        if item in produtos:
            valor_final += produtos[item]
            
    return valor_final