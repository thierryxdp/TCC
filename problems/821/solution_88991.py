def fatorial(n):
    var = [n]
    while n != 1:
        n = n - 1
        var += [n,]
    i = 0
    while i < len(var):
        mult = var[-1] * var[i-1]
        
    i = i + 1
    return mult