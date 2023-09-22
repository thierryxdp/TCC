def fatorial(num):
    '''função que calcula o fatorial do númro passado'''
    # num*(num-1)*(num-2)*(num-3)*...*2*1
    n = num
    while n != 0:
        n = n-1
    	num = num*(n)
    return num