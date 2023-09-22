def fatorial(x):
    '''A partir de um número 'x';
Calcula e retorna o resultado de x fatorial (x!);
int => int'''
    i = 1
    a = x
    while a>i:
        x= x*(a-i)
        i=i+1
    return x