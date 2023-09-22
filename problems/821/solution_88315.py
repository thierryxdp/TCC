def fatorial(n:int)->int:
    '''retorna o fatorial do valor n'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
    i+=1
    return fat