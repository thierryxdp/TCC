def fatorial(num):
    """Função que dado um numero 'num', calcula o fatorial
    desse número"""
    fatorial = 1
    while num>0:
        fatorial = fatorial * num
        num = num - 1
    return fatorial