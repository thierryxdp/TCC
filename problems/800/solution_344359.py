def total(lista_compras,produtos):
    """Retorna o valor total de uma lista de compras dado os produtos disponiveis na loja;
        list, dict -> float"""
    valor = 0
    lista_disponiveis = list(produtos.keys())
    for produto in lista_compras:
        if produto in lista_disponiveis:
            valor += produtos[produto]
    return round(valor,2)
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis