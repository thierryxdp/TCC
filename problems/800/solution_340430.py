# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras,precos_produtos):
    """Função que recebe uma lista de compras e um dicionário
       contendo o preço de cada produto disponível em uma 
       determinada loja, e retorna o valor total dos itens 
       da lista que estejam disponíveis nessa loja;
       list, dict -> float"""
    valor_total = 0
    for produto in lista_compras:
        produtos_disponiveis = list(dict.keys(precos_produtos))
        if produto in produtos_disponiveis:
            valor_total = valor_total + precos_produtos[produto]
    return round(valor_total,2)