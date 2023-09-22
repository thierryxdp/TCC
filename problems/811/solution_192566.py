def colchao(medidas,hl):
    hporta = medidas[2]
    lporta = medidas[1]
    mcolchao = medidas[0]
    hcolchao = mcolchao[0]
    lcolchao = mcolchao[1]
    ccolchao = mcolchao[2]
    if not hporta > hcolchao and not lporta > lcolchao:
        return False
    else:
        return True