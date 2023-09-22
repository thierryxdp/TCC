def fatorial(n):
    var = [n]
    while n != 1:
        n = n - 1
        var += [n,]
    return prod(var)