def dv(n,z):
    return True if n%z==0 else False
def filtro(n):
    lista = list(range(1,n+1))
    return list(map(dv,[n]*n, lista))
def qtd_divisores(n):
    return list(filter(filtro, [n]))