def  fatorial(numero):
    ''' Função calcula o fatorial de um numero indeiro qualquer,
    int --> int'''
    i = 1
    fatorial = numero
    while i < numero:
        fatorial = fatorial * i
        i += 1
    return fatorial