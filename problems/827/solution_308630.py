def qtd_divisores(n):
    '''Esta função conta quantos divisores um número n tem.
int->int'''
    total=0
    for d in range(1,n):
        if n/d==n//d:
            total=total+1
    return total