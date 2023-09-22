def fatorial(n):
    var = [n]
    while n != 1:
        n = n - 1
        var += [n,]
    produto = 1
	for numero in var:
    produto *= numero
    return produto