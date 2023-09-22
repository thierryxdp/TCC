def qtd_divisores(n):
    '''A partir do número inteiro 'n';
retorna o número de divisores inteiros que este número tem;
int => int'''
    div = 0
    for x in list(range(1,n+1)):
        if n%x == 0:
            div = div + 1
    return div