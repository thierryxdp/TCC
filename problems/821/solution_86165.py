def fatorial(n):
    '''Função calcula e retorna o fatorial de um número N;
    int->int'''
    
    fat=1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat