def dv(n,z):
    return True if z%n==0 else False
def filtro(n):
    lista = list(range(1,n+1))
    return list(map(dv, lista, [n]*n))
def qtd_divisores(n):
    return list(filter(filtro, [n]*n))