""" A função recebe nome de produtos e retorna o somatório do preço
dos produtos disponíveis em um comércio
list, dic-->float"""
def total(ls, dic):
    y=0
    for x in ls:
        y=y+dic[x]
    return round (y,2)