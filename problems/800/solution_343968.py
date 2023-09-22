# vai ver quais itens de compras desejados estão disponiveis e somá-los
def total(lc, dic):
    preco = 0
    for e in lc:
        d = dic[e]
        preco = preco + d
    return round(preco, 2)