def fatorial(n):
    c = []
    a = 1
    while a < n:
        c.append(a)
    a = a + 1
    for x in c:
         result = result * x
    return result