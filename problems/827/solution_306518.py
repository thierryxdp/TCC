def dv(n,z):
    return True if n%z==0 else False
def qtd_divisores(n):
    lista = list(range(1, n+1)
    return list(filter(dv, lista, [n]))