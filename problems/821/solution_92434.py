def fatorial(num):
    """ calcula dado valor fatorial, entrada int-->int """
    i = 1
    for num in range(2,num + 1):
        i = i * num
    return(i