def qtd_divisores(num):

    quantidade = len(filter(lambda x: num%x == 0,range(1, num+1)))
    return quantidade