def qtd_divisores(n):
    '''Conta quantos divisores um dado número tem.
int->int'''
    divisores =()
    for i in range(1,n+1):
        if n%i==0:
            divisores+=(i,)
    return len(divisores)