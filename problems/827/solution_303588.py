def qtd_divisores(n):
    '''Função que dado um numero como entrada,retorna quantos divisores ele tem.
    int->int'''
    soma=0
    for c in range(1,n+1):
        if n%c==0:
            soma=soma+1
    return soma