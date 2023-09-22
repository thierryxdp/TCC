# Questão 2
def total (lista_compras, produtos):
    ''' Retorna para nós o valor total dos itens  que estão disponíveis na loja'''
    produtos_existentes = list(produtos.keys())
        # Organizará em uma lista todos os produtos (lado direito) do dicionário
    valor = 0
    for produto in lista_compras:
        # para que o produtos esteja dentro da lista_compras (list)
        if produto in produtos_existentes:
            # e se o produto (dentro da lista) estiver na lista dos produtos_dispensa, que são os produtos do mercado
            valor += produtos[produto]
                # ele adicionará ao valor final
    return round (valor, 2)
        # nos retornará o valor somado a todos os itens somente com 2 casas decimais