def soma_h(N):
    '''Função que dado um número inteiro(N), retorna o valor de H(fórumla) com os N termos dados;
       int->float'''
    H = 0
    for i in range(1,N+1):
        fracao = (1/i)
        H = H + fracao
    return round(H,2)