def fatorial(num):
    '''Dado um número. Retorna a fatorial desse número.int-->int.'''
    i=0
    ft=1
    num1=num
    while i<num:
        ft=ft*num1
        num1=num1-1
        i=i+1
    return ft