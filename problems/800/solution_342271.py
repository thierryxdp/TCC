# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras,produtos):
    '''recebe uma lista de compras e um dicionário contendo
    os valores dos procutos disponíveis para compra. A função
    retona o valor total das compras.
    list, dic -> float'''
    soma = 0
    for item in list(dict.keys(produtos)):
        if item in compras:
            soma = soma + produtos[item]
    return round(soma,2)