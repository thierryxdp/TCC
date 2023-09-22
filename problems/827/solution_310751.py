def qtd_divisores(x):
    '''Esta função ao inserir um valor, calcula o número de
    divisores de um determinado número
    assinatura int -> int'''
    divisivel = 0
    for c in range (1, x+1):
        if x % c == 0:
            divisivel += 1
    return divisivel