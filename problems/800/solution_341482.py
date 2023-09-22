def total(lista,produto):
    """função que retorna o valor somado dos itens disponiveis
    list, dict -> int"""
    soma = 0.00
    for x in lista:
        a = produto(lista)
        soma = soma + a
        soma = round(soma,2)
        return soma