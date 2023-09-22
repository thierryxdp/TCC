def soma_h(n):
    '''função que calcula e rotorna o valor de H, com N termos,
    onde N é inteiro e dado como entrada da função.
    int,->int'''
    soma=0
    for i in range(1,n+1):
        soma=soma+1/i
        resultado = round(soma,2)
    return resultado