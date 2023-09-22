def qtd_divisores(num):
    a = 1
    while a <= num:
        x = num % a
        a = a +1
        if x == 0:
            u = [a-1]
            print u