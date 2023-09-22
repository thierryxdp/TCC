def qtd_divisores(n):
    '''Função que conta quantos divisores um número tem. Este número será passado como entrada'''
    for i in range(1, n//2+1):
        if n % i == 0:
            yield i
    yield n