def total(lista,valores):
    '''Funcao que recebe uma lista de compras (lista) e um dicionario com o preco dos produtos, e retorna o valor total da compra; list(str, str, str...), dict(str:float, str:float,...) -> float'''
    pag=0
    for produto in lista:
        precos=dict.get(valores,produto)
    return sum(precos)