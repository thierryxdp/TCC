def total(lista_de_compras,itens_disponiveis):
    """Funcao que recebe uma lista de compras e um dicionario
    contendo o preco de cada produto disponivel em determorinada
    loja, retorna o valor total dos itens da lista que estejam
    disponiveis na loja;
    list, dict -> float"""
    valor_total=(0)
    for produto in lista_de_compras:
        if produto in itens_disponiveis:
            valor_total+=(itens_disponiveis[produto])
    return valor_total