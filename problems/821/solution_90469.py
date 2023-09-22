def fatorial(num):
    'calcula o fatorial de um número'
    'int -> int'
    c=num
    i=1
    while c>0:
        i=i*c
        c=c-1
    return i