def qtd_divisores(n):
    '''FunÃ§Ã£o que calcula a quantidade de divisores
    que um nÃºmero possui (int -> int)'''
    y = []
    for x in range(1, n+1):
        if n%x == 0:
            y.append(x)
    return