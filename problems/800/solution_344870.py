# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras,precos_produtos):
    '''Dada uma lista de compras e um dicionário contendo o preço dos produtos de uma loja. Retorna o valor total dos itens da lista que estejam disponíveis nesta loja
    list,dict -> float'''
    total = 0
    for i in range(len(lista)):
        total += float(produtos[lista[i]])
    return round(total,2)