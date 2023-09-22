def soma_h(n):
    '''a função retorna a soma dos invesos do número recebido
    int->float'''
    i = 1
    h = 0
    while i <= n:
        h = h + 1/i
        i += 1
    return round(h,2)