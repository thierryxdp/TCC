def qtd_divisores(num):
    '''função recebe como entrada um número e retorna a
    quantidade de divisores que possui
    int->int'''
    i = 1
    mdc = 1 #o Próprio num
    while i < num:
        if num%i==0:
            mdc += 1
        i += 1
    return mdc