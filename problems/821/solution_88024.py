def fatorial(num):
    '''função que calcula o fatorial do númro passado'''
    # num*(num-1)*(num-2)*(num-3)*...*2*1
    k = num
    while k > 0:
        num = num*(num-1)
        k -= 1
    return num