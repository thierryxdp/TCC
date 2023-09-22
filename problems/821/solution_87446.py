def fatorial(numero):
    '''calcula o fatorial do numero dado.
    int -> int'''
    produto = 1
    while 0 < numero:
        produto = produto*numero
        numero -= 1
    return produto