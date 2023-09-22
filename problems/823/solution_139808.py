def faltante(ls):
    m = max(ls) +1
    soma = sum(range(m)) - sum(ls)
    return m if soma == 0 else soma