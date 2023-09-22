def soma_h(n):
    '''calcula e retorna o valor h de uma conta matemática com n termos onde n é inteiro e é dado como parâmetro de entrada;int->float'''
    h=1
    for c in range(2,n+1):
        h+=1/c
    return round(h,2)