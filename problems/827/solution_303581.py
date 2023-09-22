def qtd_divisores(n):
    '''Função que conte quantos divisores um dado número inteiro tem.
int, int'''
    qtd = 1
    for i in range(1,n//2+1):
        if n % i == 0:
            qtd += 1
        return qtd