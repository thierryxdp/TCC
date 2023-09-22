def qtd_divisores(n):
    '''função que conte quantos divisores um número tem.
    Exemplo: Se o número for 10, os divisores são: 1, 2, 5 e 10; total de 4 divisores.
    int-->int'''
    dicio=range(1,n+1)
    soma=0
    for i in range(1,n+1):
        d=n/i
        if d in dicio:
            soma+=1
    return soma