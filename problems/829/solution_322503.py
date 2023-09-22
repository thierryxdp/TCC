def soma_h(n):
    ''' funcao calcula 1+somatorio de 1/n, int-->float'''
    somatorio=0
    for i in range(n+1):
        if n>0:
            somatorio= somatorio+ 1/i
    return soma