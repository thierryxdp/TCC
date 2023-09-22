def qtd_divisores(n):
    '''retorna a quantidade de divisores de n'''
    d = [(n%i) for i in range(1, n+1)]
    return d.count(0)