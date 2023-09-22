# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras, precos):
    """Recebe uma lista de compras e um dicionário com os preços dos produtos da loja e retorna
    o valor total dos itens da lista.
    list, dictionary -> float"""
    i = 0
    for x in compras:
        if x in precos:
            i = i + precos[x]
    return round(i, 2)