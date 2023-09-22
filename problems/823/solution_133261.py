def faltante(l):
    i = 1
    atual = 1
    while i in l:
        i = atual
        atual = atual + 1
    return atual