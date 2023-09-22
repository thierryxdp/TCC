def filtra_pares(tup):
    '''Função que recebe uma tupla com quatro elementos inteiros 
    como parâmetro e retorna uma nova tupla contendo apenas os elementso
    pares da tupla original na mesma ordem em que se encontravam;
       tup -- tup'''
    if len(tup) == 4:
        return (tuple(filter(lambda x: x % 2 == 0, tup)))