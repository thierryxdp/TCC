def total(lista,precos):
    """Para cada item na lista recebida, verifica se está no dicionário
    de preços, caso sim, adiciona o valor do item no dicionário ao valor
    anterior (começando com valor=0), após verificar todos itens a lista
    retorna o preço em 2 casas decimais.
    lista, dicionário-> float"""
    valor=0
    for item in lista:
        if item in precos:
            valor+=precos[item]
    return round(valor,2)