def total(lista,dici):
    '''recebe uma lista de compras e um dicionário com o preço de cada produto da lista que existe na loja e retorna o valor total dos itens que estão na lista e na loja ao mesmo tempo, com aproximação decimal de 2 casas;
    list, dict -> float'''
    soma = 0
    for produto in lista:
        if produto in dici:
            soma = soma + dici[produto]
    return round(soma,2)