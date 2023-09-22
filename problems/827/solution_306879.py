def qtd_divisores(n):
    '''retorna a quantidade de divisores de n'''
    d = [(i if n%i==0) for i in range(1, n+1)]
    return len(d)