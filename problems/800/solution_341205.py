# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,precos):
    """ Esta Função recebe uma lista de compras (lista cujas strings dentro
    representam os produtos a serem comprados) e um dicionário com os preços de
    cada item em uma loja. A função retorna o valor total das compras
    list,dict->float"""
    valor=0
    for item in lista:
        valor=valor+precos[item]
    return round(valor,2)