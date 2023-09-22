def dv(n,z):
    return True if n%z==0 else False
def filtro(n):
    lista = list(range(1, n+1))
    return list(map(dv, lista, [n]*len(lista)))
def qtd_divisores(n):
    return len(list(filter(filtro, [n])))