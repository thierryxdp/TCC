def fatorial(num):
    """função que recebe um número qualquer (num) e calcula o seu
    fatorial;
    int->int"""
    i= 0
    num_2 = num
    while (num-i)>1:
        num_2 = num_2*(i+1)
        i = i+1
    return num_2