def colchao(medidas,H,L):
    hporta = H
    lporta = L
    mcolchao = medidas
    hcolchao = mcolchao[0]
    lcolchao = mcolchao[1]
    ccolchao = mcolchao[2]
    if hporta < ccolchao and lporta < lcolchao and hporta < lcolchao:
        return False
    else:
        return True