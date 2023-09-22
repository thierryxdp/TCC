def dv(n,z):
    return True if n%z==0 else False
def qtd_divisores(n):
    lista = list(range(1,n+1))
    k = filter(list(map(dv,[n]*n, lista)),lista)
    return list(k)
#def qtd_divisores(n):
   # return list(filter(filtro*n, [n]))