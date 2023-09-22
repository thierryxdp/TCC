def fatorial(n):
    num = list(range(n+1))
    num.pop(0)
    x = 0
    resultado = 1
    while len(num) > x:
        resultado = resultado * num.pop(0)
    return resultado