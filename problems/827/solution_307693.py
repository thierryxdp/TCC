def qtd_divisores(n):
    '''Uma função que ao recebe um numero retorna a quantidade
    de divisores int ->int'''
    soma=0
    for i in range(1,n+1):
        if n % i == 0:
            soma+=1
    return soma