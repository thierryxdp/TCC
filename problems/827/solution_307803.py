def qtd_divisores(num):
    '''Conta quantos divisores um número tem.
    int->int
    '''
    div=0
    for x in range(1,num+1):
        if num%x==0:
            div+=1
    return div