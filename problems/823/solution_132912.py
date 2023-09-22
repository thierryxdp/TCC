def faltante(l):
    n = len(l) + 1
    somatotal = n * (n + 1) // 2
    return somatotal - sum(l)