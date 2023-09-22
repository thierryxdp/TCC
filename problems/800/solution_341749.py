# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras, preco_produto):
    '''Função que recebe como entrada uma lista de compras e um dicionário contendo
    o preço de cada produto disponível em uma determinada loja, e retorna o valor
    dos itens disponíveis nesta loja; lista;dict->float'''
    valor_total=0
    for i in lista_de_comprar:
        if i in preco_produto:
            valor_total+=preco_produto[i]
    return round(valor_total,2)