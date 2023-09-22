def total(comprar, disponivel):
    '''Retorna a soma dos itens de uma lista disponíveis em um determinado mercado: list, dict --> float'''
    soma = 0
    for item in comprar:
        if item in disponivel:
            soma = soma + disponivel[item]
    return soma