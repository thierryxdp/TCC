def total(lista,produto):
    """função que retorna o valor somado dos itens disponiveis
    list, dict -> int"""
    soma = 0.00
    indice = 0
    while indice<len(lista):
        a = produto[lista[indice]]
        soma = soma + a
        indice = indice + 1
    soma = round(soma,2)
    return soma