def fatorial(num):
    '''Funcao que calcula o fatorial de um numero X sem usar a funcao fatorial do modulo math'''
    fat_variavel = 1 
    i = 2 
    while i <= num:
        fat_variavel = fat_variavel*i
        i = i + 1
    return fat_variavel