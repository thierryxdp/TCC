def total(lista,dicionario):
    ''' função que recebe como entrada uma lista contendo itens, em string,
e um dicionario contendo mapeamentos onde cada chave é um produto disponível,
e o valor do mapeamento é o preço do produto; retorna o valor total a pagar pelos
itens da lista que estão disponíveis no dicionário; list,dict->float'''

    soma=0

    for produto in lista:
        if produto in dicionario:
            soma=soma+dicionario[produto]
    return soma