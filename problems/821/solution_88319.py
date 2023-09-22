def fatorial(n:int)->int:
    '''retorna o fatorial de n'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print(fat)