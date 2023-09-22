def soma_h(N):
    '''Calcula o valor da expressão H. Assinatura: int->float'''
    s=0
    for x in range(N):
        s = s + 1/(x+1)
    return round(s,2)