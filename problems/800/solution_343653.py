def total(lista_compras, dicionario):
    """
    Essa função recebe uma lista de compras e um dicionario contendo os 
    precos de cada produto disponível em uma determinada loja, e retorna
    o valor total doos itens da lista que esteam disponiveis na loja
    Parametros de entrada: list, dic
    Valor de Retorno: int
    """
    total=[]
    soma=0
    for produto in lista_compras:
        round(soma,2)
        soma = soma + dicionario[produto]
        
    return soma