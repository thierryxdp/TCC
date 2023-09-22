def total(lista,dic):
    '''função que recebe uma lista de compras e um dicionario contendo o preço de cada produto, retornando o valor total dos itens da lista disponiveis na loja.
    list, dict -> float
    Explicação: verifica se um elemento está na lista, se estiver procura por ele no dicionario e depois soma os valores dos itens.'''
    soma = 0
    for e in lista:
      e=dic[e]
      soma=soma+e
    return round(soma,2)