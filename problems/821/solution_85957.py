def fatorial(num):
    
#retorna o fatorial de um número dado    

    fat = 1

    while 0 < num-1:
        fat = fat * num
        num -= 1

    return fat