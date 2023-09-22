def total(compras,precos):
    """Calcula e retorna o valor total dos itens da lista "compras" que
    estejam disponiveis na loja, dado um dicionario, "precos", contendo
    o valor de cada produto"""
    soma=0
    for i in range(len(compras)):
        if compras[i] in precos:
            soma= round((soma+ precos[compras[i]]),2)
    return soma