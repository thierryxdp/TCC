def fatorial(numero):
    '''calcula o fatorial de um número inteiro recebido.
    int -> int'''
	num = 1
    total = 1
    while num <= numero:
        total = total * num # acumulador 
        num = num + 1 #contador
    return total