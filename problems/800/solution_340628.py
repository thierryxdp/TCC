def total(lista,dicionario):
    """Dada uma lista de compras, com o nome dos produtos, e um dicionário
    com o nome e os respectivos preços dos produtos, a função retorna o valor
    total dos itens da lista que estejam disponíveis no dicionário.
       A lista deve ser escrita entre colchetes e o dicionário entre chaves;
       list,dic --> float"""
    valor = 0
    for produtos in lista:
        valor = valor + dicionario[produtos]
    return round(valor,2)