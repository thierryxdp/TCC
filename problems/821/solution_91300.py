def fatorial(num):
    while num > 0:
        fat = 1
        while num > 1:
            fat = fat  + num
            num = num + 1
        return fat