def fatorial(n:int)->int:
    '''retorna o fatorial do valor n'''
    fat = 0
    i = 1
    while i <= n:
        fat = fat*i
    i+=1
    return fat