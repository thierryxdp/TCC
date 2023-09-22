def total(lc, tabela):
    custo = 0
    for p in lc:
        custo += dict.get(tabela, p, 0)
    return round(custo,2)