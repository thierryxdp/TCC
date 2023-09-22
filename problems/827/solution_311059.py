def qtd_divisores(num):
    '''jjj'''
    j=0
    for i in range(1, num//2+1):
        if num % i == 0:
            j=j+i
    return j