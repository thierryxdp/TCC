def fatorial(numero):
    '''que dado um numero, calcula o fatorial dele
    int -> int'''
    num = 1
    total = 1
    while num <= numero:
        total = total * num # acumulador 
        num = num + 1 #contador
    return total