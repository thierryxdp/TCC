# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,preços):
    '''Dado uma lista de compras e um dicionário contendo
o preço de cada produto disponível em determinada loja,
retorna o valortotal dos itens da lista que estão disponíveis
na loja. list, dict ->float'''
    total=0
    for item in lista:
        if item in preços:
            total+=preços[item]
    return total