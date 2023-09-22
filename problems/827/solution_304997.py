def qtd_divisores(n):
    '''funcao q conta quants divisores um numero tem'''
    cont = 0 
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
    return cont