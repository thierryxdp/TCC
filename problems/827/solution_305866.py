def qtd_divisores(x):
    '''Função que recebe um número e conta quantos divisores ele tem.
    entrada da função: int
    saída da função: int'''
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    yield num