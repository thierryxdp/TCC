def fatorial(n):
    "Calcula o fatorial de um número"
    nf = 1
    count = 1
    while count < n+1:
        nf = nf * count
        count = count + 1
    return nf