def qtd_divisores (n):
    '''Essa fornece quantos divisores um número possui'''
    '''int -> int'''
    d= []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(d,i)
    return len(d)