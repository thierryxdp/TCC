def total(lista, d):
    """ Funçao que retorna o valor total dos itens de uma lista que esteja
disponivel em uma loja"""

numero_preco = 0
    for i in lista:
        if i in d:
            numero_preco = numero_preco + d[i]
        else:
            numero_preco = numero_preco
            return round(numero_preco,2)