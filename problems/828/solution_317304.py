def primo (n):
    '''função que dada um numero inteiro positivo diz se ele é primo; int ->bool'''
    qtd = 0
    for divisor in range(n,n+1):
        if n%divisor==0:
            qtd += 1
    if qtd>2:
        return False
    else:
        return True