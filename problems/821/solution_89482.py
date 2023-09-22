def fatorial(num):
    '''Dado um número. Retorna a fatorial desse número.int-->int.'''
    i=0
    ft=1
    while i<num:
        ft=ft*num
        num=num-1
        i=i+1
    return ft