def fatorial(n):
    ''' funcao que calcula o fatorial (n)
int -> int'''
    fat =1
    assert (type(n) is int) and (n >= 0), 'inteiro e positivo'
    while (n>0):
        fat = fat*n
        n = n -1
    return fat