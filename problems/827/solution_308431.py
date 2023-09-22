def total_divis(n):
    '''Função que conta quantos divisores um dado número inteiro tem;
       int --> int'''
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(a,i)
    return len(a)