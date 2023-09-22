def soma_h(n):
    'Função que recebe um número N e retorna a soma de [1^(-1)] a [N^(-1)].'
    'int->float'
    h=0
    for n in range(1,n+1):
        h=h+(1/n)
    return round(h,2)