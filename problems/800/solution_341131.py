# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, loja):
    '''recebe uma lista de compras(lista) e um dicionario contendo
    todos os produtos disponiveis em uma loja, retorna o valor total
    dos itens da lista que estejam disponiveis na loja;
    list, dict -> dict'''
    lista2 = {}
    soma = 0
    for produto in lista:
        if produto in loja:
            soma += dict.get(loja,produto)
    round(soma,2)
    return soma