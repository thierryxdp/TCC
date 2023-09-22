def fatorial(num):
    'calcula o fatorial de um numero; int->int'
    l=1
    while num >=1:
        l=l*num
        num=num-1
    return l