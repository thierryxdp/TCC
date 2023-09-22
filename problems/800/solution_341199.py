# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras,preco_itens):
    """retorna o valor total dos itens da lista que estejam disponiveis;
    list, dict -> float"""
    p=0
    for x in lista_compras:
        if x in preco_itens:
            p=p+dict.get(preco_itens,x)
    return p