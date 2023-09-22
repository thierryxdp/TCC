def soma_h(n):
    '''calcula e retorna o valor H com N
    int->float'''
    soma=0
    for c in range(1,n+1):
        soma+=1/c
    return round(soma,2)