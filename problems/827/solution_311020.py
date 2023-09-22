def qtd_divisores(n):
    '''um programa que conte quantos divisores um dado número tem.'''
    #int > int
    total = [n,]
    index = 1
    for index < n:
        if (n%index) == 0:
            total = total + [index]
        index = index + 1
        return len(total)
        else:
            return 0