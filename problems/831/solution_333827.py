""" dada uma palavra, a função retorna sua tradução na língua do p
list, dic-->float"""

def total(ls, dic):
    y=0
    for x in ls:
        y=y+dic[x]
    return round(y, 2)