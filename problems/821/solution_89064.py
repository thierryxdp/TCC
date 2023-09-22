def fatorial(n):
    var = [n]
    while n != 1:
        n = n - 1
        var += [n,]
    i = 0
    while i < len(var):
        var[i] * var[i-1]