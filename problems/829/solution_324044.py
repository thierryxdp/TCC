def somaH(n):
    '''Funçao que calcula a soma de H (int -> float)'''
    if type(n) != 'int':
        return 'Insira um nÃºmero inteiro!'
    y = [1]
    for x in range(2, n+1):
        y.append(1/x)

    return sum(y)