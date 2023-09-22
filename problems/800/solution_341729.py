def total(item,dicio):
    '''Função que recebe uma lista de compras e um dicionário
       contendo o preço de cada produto disponível em uma 
       determinada loja, e retorna o valor total dos itens
       da lista que estejam disponíveis na loja.
       : param item: list
       : param dicio: dict
       : return: float
    '''
    soma=0
    for el in item:
        if el in dicio:
            soma= soma + dicio[el]
    return round(soma,2)