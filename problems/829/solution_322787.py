def soma_h(n):
    '''Função que recebe um número inteiro e retorna o valor H com N
    termos. H=1 + 1/2 +1/3 + ... +1/n. int->float'''
    H=0
    for i in range (1,n+1):
        H = H + 1/i
    return round(H,2)