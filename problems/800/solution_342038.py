def total(lista,dicionario):
    """
    Função que recebe uma lista de compras e um dicionário contendo os preços de uma determinada
    loja. Com isso, retornaremos o valor total do que seria uma compra dos produtos disponíveis.
    list, dict -> int
    """
    
    soma = 0
    for produto in lista:
        if produto == dicionario:
            soma = soma + dicionario[produto]          
    return soma