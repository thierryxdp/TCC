def fatorial(num):
    """Função que recebe um número e retorna o fatorial. Use int -> int: 5 -> 120"""
    c = cont = 1
    while cont < num:
        cont += 1
        c *= cont
    return c
    # c = 1
    # for x in range(1,num+1):
    #     c*=x
    # return c