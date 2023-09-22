# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, dici):
    '''função em que dado uma lista e um dicicionário
    contendo o preço de cada produto, retorna o valor total
    dos itens da lista; list, dici --> int'''
    produto = 0
    for i in range (len(lista)):
        if lista[i] in dict.keys(dici):
            produto = produto + dict.get(dici, lista[i])
            final = round(produto, 2)
    return final