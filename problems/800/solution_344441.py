""" Dada uma lista de compras, a função retorna o preço total dos produtos disponíveis"""
#list, dic-->float

def total(ls,dic):
    y=0
    for x in ls:
        y=y+dic[x]
    return round