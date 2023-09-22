def soma_h(n):
    ''' funcao calcula 1+somatorio de 1/n, int-->float'''
    soma=0
    for i in range(n+1):
        if n>0:
            soma=soma+1/i
    return soma