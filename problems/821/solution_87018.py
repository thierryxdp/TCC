def fatorial(num):
    ''' Calcula o fatorial do numero fornecido sendo ele > 0;
    int -> int'''
    i = 1
    num_fat = 1
    while i <= num:
        num_fat *= i
        i += 1
    return num_fat