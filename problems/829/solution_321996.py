def f(x):
    return 1/x
def soma_h(N):
    lista = list(map(f, range(1, N+1)))
    return round(sum(lista), 2)