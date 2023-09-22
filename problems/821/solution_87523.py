def fatorial(n):
    num = list(range(5))
    num.pop(0)
    x = 0
    resultado = 0
    while len(num) > x:
        resultado = resultado * num.pop(0)
        x += 1
    return resultado