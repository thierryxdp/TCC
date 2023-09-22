def qtd_divisores(num):
    '''retorna a quantidade de divisores naturais um numero tem
    int->int'''
    counter = 0
    for x in range(num,0,-1):
        if x%num == 0:
            counter += 1
    return counter