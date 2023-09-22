def fatorial(num):
    """calcula e retorna o fatorial de um numero;
    int->int"""
    i = 1
    numFatorial = 1
    while i <= num:
        numFatorial = numFatorial*i
        i = i + 1
    return numFatorial