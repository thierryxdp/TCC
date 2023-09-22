def fatorial(num):
    '''função que calcula o fatorial do númro passado'''
    # num*(num-1)*(num-2)*(num-3)*...*2*1
    for i in range(num):
        num = num*(num-1)
    return num