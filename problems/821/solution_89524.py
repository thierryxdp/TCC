def fatorial(numero):
    '''calcula o fatorial de um número inteiro recebido.
    int -> int'''
    num = 1
    total = 1
    while num <= numero:
        total = total * num 
        num = num + 1 
    return total