def qtd_divisores(n):
    '''Conta quantos divisores um dado número tem.
int->int'''
    if n<0:
        n=(n*-1)
    divisores=()
    i=1
    while i<n+1:
        if n%i==0:
            divisores+=(i,)
        i+=1
    return len(divisores)
qtd_divisores(-20)