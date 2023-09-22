def total(list = [], dict = {}):
#Dada uma lista e um dicionario respectivamente, é retornado o valor de itens de compras da lista list, dict -> int
    valor = 0
    for n in list:
        if n in dict:
            valor = valor + (dict.setdefault(n))
    return round(valor, 2)