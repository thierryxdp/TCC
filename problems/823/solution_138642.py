def soma(l):
    s = max(l) + min(l)
    n = max(l)
    return s*n/2

def faltante(l):
    somatorio = soma(l) - sum(l)
    if somatorio == 0:
        return len(l)+1
    else:
        return int(somatorio)