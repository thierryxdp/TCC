# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras, produtos):
    """Recebe uma lista de comprar e os produtos da loja e retorna o valor
    total a se pagar de acordo com lista;
    tuple<str>[???], dict --> float"""

    total = 0
    for produto in lista_de_compras:
        if produto in produtos:
            total += float(produtos[produto])

    return round(total, 2)