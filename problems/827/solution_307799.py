def qtd_divisores(num):
    '''Conta quantos divisores um número tem.
    int->int
    '''
    div=0
    for x range(num):
        if num%2==0:
            div+=1
    return div