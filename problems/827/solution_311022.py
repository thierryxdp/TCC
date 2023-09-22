def qtd_divisores(n):
    '''um programa que conte quantos divisores um dado número tem.'''
    #int > int
    total = [n,]
    index = 1
    while index < n:
        if (n%index) == 0:
            total = total + [index]
        index = index + 1
        return len(total)
	for index in n:
        if n == 0 or n < 0:
            return 0