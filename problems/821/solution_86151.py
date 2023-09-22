def fatorial (n):
    '''Calcula e retorna o fatorial do número "n" inserido;
    int -> int'''
    fatorial = 1
    count = 1
    while count <= n:
        fatorial *= count
        count += 1
    return (fatorial)