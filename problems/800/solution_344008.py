# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef total(lista, dicionario):
def total(lista,dicionario):
    """Recebe uma lista de compras e um dicionário contendo o preço dos produtos em uma loja, e retorna o valor total dos itens a lista que estão nessa loja

    list, dict -> int"""

    acumulador = 0

    contador = 0

    for numero in range(len(lista)):

        compra = lista[contador]

        valor = dict.get(dicionario, compra)

        acumulador = acumulador + valor        

        contador = contador + 1   

    return round(acumulador, 2)