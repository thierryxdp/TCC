def total(lista,dic):
    'recebe uma lista de compras e um dicionário contendo o preço de cada produto em uma loja, retorna valor dos itens da lista'
    soma = 0
    for coisa in lista:
        if coisa in dic:
            soma = soma + dic[coisa]
    return round(soma, 2)